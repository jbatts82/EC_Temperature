###############################################################################
# File Name  : temperature.py
# Date       : 04/24/2021
# Description: Temperature Data
###############################################################################


import control.room_control as rc
import data.db_app as db
from datetime import datetime
from support import log
from support import div
import collections
import numpy as np


def Init_Temperature(config):
    global temp_data, cache, count, time_table, rolling_avg_size

    sensor_cnt = len(config.dht11_config)
    rolling_avg_size = config.ROLLING_AVG_SIZE
    time_table = config.time_table

    temp_data = {}
    for sensor in range(sensor_cnt):
        channel = config.dht11_config[sensor]['name']
        temp_data[channel] = {
            'previous_temperature' : None,
            'max_temperature' : 0,
            'min_temperature' : 99,
            'rolling_avg' : 0,
            'minute_avg' : 0,
            'heater_state' : False,
        }

    cache = {}
    count = {}
    for each in config.dht11_config:
        cache[each["name"]] = collections.deque(maxlen=config.DEQUE_SIZE)
        count[each["name"]] = 0

def Process_Temperature(new_data):
    global temp_data, cache, count, rolling_avg_size

    channel = new_data["name"]
    temperature = new_data["temp"]
    time = new_data["time"]
    write_to_db = False

    if temp_data[channel]['previous_temperature'] == None:
        temp_data[channel]['previous_temperature'] = temperature
        return write_to_db

    delta = abs(temp_data[channel]['previous_temperature'] - temperature)

    if delta > 5:
        print("!!!!!!!!!!!!!!!!!NOT PLAUSIBLE!!!!!!!!!!!!!!!!!!!!!")
        return write_to_db

    temp_data[channel]['previous_temperature'] = temperature

    cache[channel].append(temperature)

    mean = running_mean(cache[channel], rolling_avg_size)

    count[channel] = count[channel] + 1

    if not mean:
        return write_to_db

    if (count[channel] % 4) != 0:
        return write_to_db

    write_to_db = True

    log("{} Readings".format(channel), count[channel])

    average_temp = mean.item()

    log("{} Average".format(channel), average_temp)

    temp_setting = get_temp_setting()

    min_temp_threshold = temp_setting['temp']

    if channel == "ch1":
        if temp_data[channel]['heater_state'] == False:
            if average_temp < min_temp_threshold:
                rc.Request_Heater_On("temperature")
                temp_data[channel]['heater_state'] = True
                rc.Request_Fan_Off("temperature")
                log("!!!HEATER!!!", temp_data[channel]['heater_state'])
        else:
            if average_temp > (min_temp_threshold + 2):
                rc.Request_Heater_Off("temperature")
                temp_data[channel]['heater_state'] = False
                log("!!!HEATER!!!", temp_data[channel]['heater_state'])

    return write_to_db

def get_temp_setting():
    global temp_data, time_table
    date_time_now = datetime.now()
    hour_now = date_time_now.hour
    for hour in time_table[::-1]:
        if hour_now >= hour["hour"]:
            break
    temp_setting = hour
    return temp_setting

def running_mean(x, N):
    global cumsum
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)
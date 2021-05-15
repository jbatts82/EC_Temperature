###############################################################################
# File Name  : temperature.py
# Date       : 04/24/2021
# Description: Humidity Data
###############################################################################


import control.room_control as rc
import data.db_app as db
from datetime import datetime
from support import log
from support import div
import collections
import numpy as np

global temp_data, cache, count


def Init_Temperature(config):
    global temp_data, cache, count

    temp_data = {
        'rolling_avg_size' : config.ROLLING_AVG_SIZE,
        'max_temperature' : 0,
        'min_temperature' : 0,
        'rolling_1min' : 0,
        'heater_state' : False,
        'time_table' : config.time_table
    }

    cache = {}
    count = {}
    for each in config.dht11_config:
        cache[each["name"]] = collections.deque(maxlen=config.DEQUE_SIZE)
        count[each["name"]] = 0

def Process_Temperature(new_data):
    global temp_data, cache, count
    channel = new_data["name"]
    temperature = new_data["temp"]
    time = new_data["time"]

    cache[channel].append(temperature)
    mean = running_mean(cache[channel], temp_data['rolling_avg_size'])
    count[channel] = count[channel] + 1

    if not mean:
        return

    if (count[channel] % 4) != 0:
        return

    log("{} Readings".format(channel), count[channel])

    average_temp = mean.item()

    log("{} Average".format(channel), average_temp)

    db.Write_Instant_Temp(time, channel, average_temp)

    temp_setting = get_temp_setting()
    min_temp_threshold = temp_setting['temp']


    if channel == "ch1":
        if temp_data['heater_state'] == False:
            if average_temp < min_temp_threshold:
                rc.Request_Heater_On("temperature")
                temp_data['heater_state'] = True
                rc.Request_Fan_Off("temperature")
                log("!!!HEATER!!!", temp_data['heater_state'])
        else:
            if average_temp > (min_temp_threshold + 3):
                rc.Request_Heater_Off("temperature")
                temp_data['heater_state'] = False
                log("!!!HEATER!!!", temp_data['heater_state'])

    if channel == "ch2":
        pass

    if channel == "ch3":
        pass

    if channel == "ch4":
        pass

def get_temp_setting():
    global temp_data
    time_table = temp_data['time_table']
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
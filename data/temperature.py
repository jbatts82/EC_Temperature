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
import pandas as pd

# x = array
# N = max number of elements
def rolling_avg(x, N):
    y = np.zeros((len(x),))
    for ctr in range(len(x)):
         y[ctr] = np.sum(x[ctr:(ctr+N)])
    return y/N

def running_mean(x, N):
    global cumsum
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

class Temperature:
    def __init__(self, config):
        self.the_config = config
        self.rolling_avg_size = self.the_config.NUM_ELMTS
        self.cache = {}
        for each in self.the_config.dht11_config:
            self.cache[each["name"]] = collections.deque(maxlen=self.rolling_avg_size)

        self.max_temperature = 0
        self.min_temperature = 99
        self.rolling_1min = 0
        self.config = config
        self.heater_state = False

    def process_new_data(self, data):
        channel = data["name"]
        temperature = data["temp"]
        time = data["time"]

        self.cache[channel].append(temperature)

        mean = running_mean(self.cache[channel], self.rolling_avg_size)

        if mean:
            average_temp = mean.item()
            log("{} Average".format(channel), average_temp)

            db.Write_Instant_Temp(time, channel, average_temp)

            temp_setting = self.get_temp_setting()
            min_temp_threshold = temp_setting['temp']
            log("Min Temp Thresh", min_temp_threshold)

            if channel == "ch1":
                if self.heater_state == False:
                    if average_temp < min_temp_threshold:
                        rc.Request_Heater_On("temperature")
                        self.heater_state = True
                        rc.Request_Fan_Off("temperature")
                        log("!!!HEATER!!!", self.heater_state)
                else:
                    if average_temp > (min_temp_threshold + 3):
                        rc.Request_Heater_Off("temperature")
                        self.heater_state = False
                        log("!!!HEATER!!!", self.heater_state)

            if channel == "ch2":
                pass

            if channel == "ch3":
                pass

            if channel == "ch4":
                pass

    def get_temp_setting(self):
        time_table = self.the_config.time_table
        date_time_now = datetime.now()
        hour_now = date_time_now.hour
        
        for hour in time_table[::-1]:
            if hour_now >= hour["hour"]:
                break

        temp_setting = hour

        return temp_setting
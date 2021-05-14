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

            log(channel, mean.item())

            db.Write_Instant_Temp(time, channel, mean.item())

            if channel == "ch1":
                if self.heater_state == False:
                    if temperature < 69:
                        rc.Request_Heater_On("temperature")
                        self.heater_state = True
                        rc.Request_Fan_Off("temperature")
                        log("!!!HEATER!!!", self.heater_state)
                else:
                    if temperature > 71:
                        rc.Request_Heater_Off("temperature")
                        self.heater_state = False
                        log("!!!HEATER!!!", self.heater_state)

            if channel == "ch2":
                pass

            if channel == "ch3":
                pass

            if channel == "ch4":
                pass
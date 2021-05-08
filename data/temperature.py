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


class Temperature:
    def __init__(self, config):
        self.max_temperature = 0
        self.min_temperature = 99
        self.rolling_1min = 0
        self.config = config
        self.heater_state = False
        self.temp_info = []

    def process_new_data(self, data):
        channel = data["name"]
        temperature = data["temp"]
        time = data["time"]

        db.Write_Instant_Temp(time, channel, temperature)

        if channel == "ch1":
            #print(self.temp_info)
            log("Process {} ".format(channel), "Time: {} Temp: {}".format(time, temperature))
            if self.heater_state == False:
                if temperature < 70:
                    rc.Request_Heater_On("temperature")
                    self.heater_state = True
                    rc.Request_Fan_Off("temperature")
                    log("!!!HEATER!!!", self.heater_state)
            else:
                if temperature > 74:
                    rc.Request_Heater_Off("temperature")
                    self.heater_state = False
                    log("!!!HEATER!!!", self.heater_state)

       
    def calculate_avg_temperature(self):
        self.avg_temperature = (self.instant_temperature1 + self.instant_temperature2) / 2
    
    def get_average_temperature(self):
        return self.avg_temperature
        
    def get_temperature1(self):
        return self.instant_temperature1
    
    def get_temperature2(self):
        return self.instant_temperature2
        
    def is_max(self, temperature):
        if temperature > self.max_temperature:
            self.max_temperature = temperature
            
    def is_min(self, temperature):
        if temperature < self.min_temperature:
            self.min_temperature = temperature
        
    def get_min_temperature(self):
        return self.min_temperature
        
    def get_max_temperature(self):
        return self.max_temperature
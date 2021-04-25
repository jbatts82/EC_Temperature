###############################################################################
# File Name  : temperature.py
# Date       : 04/24/2021
# Description: Humidity Data
###############################################################################

from control.heater import Heater
from datetime import datetime
from support import log
from support import div

class Temperature:
    def __init__(self, config):
        self.max_temperature = 0
        self.min_temperature = 99
        self.avg_temperature = 0
        self.config = config
        self.heater = Heater(self.config)
        self.heater_state = False
        self.temperature_data = []

    def process_new_data(self, data):
        channel = data["name"]
        temperature = data["temp"]
        time = data["time"]

        # self.temperature_data.append(data)
        # log("TempArr", len(self.temperature_data))

        log("Process {} ".format(channel), "Time: {} Temp: {}".format(time, temperature))

        if channel == "ch1":
            if self.heater_state == False:
                if temperature < 70:
                    self.heater.Turn_On()
                    self.heater_state = True
                    log("HEATER", self.heater_state)
            else:
                if temperature > 75:
                    self.heater.Turn_Off()
                    self.heater_state = False
                    log("HEATER", self.heater_state)

       
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
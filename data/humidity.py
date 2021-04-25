###############################################################################
# File Name  : humidity.py
# Date       : 04/24/2021
# Description: Humidity Data
###############################################################################

from control.humidifier import Humidifier
from datetime import datetime
from support import log
from support import div

class Humidity:
    def __init__(self, config):
        self.config = config
        self.max_humidity = 0
        self.min_humidity = 99
        self.five_min_avg_humidity = 0
        self.instant_humidity = 0
        self.humidifier_state = False
        self.humidifier = Humidifier(self.config)

    def process_new_data(self, data):
        channel = data["name"]
        humidity = data["hum"]
        time = data["time"]

        log("Process {} ".format(channel), "Time: {} Hum: {}".format(time, humidity))


        if channel == "ch1":
            if self.humidifier_state == False:
                if humidity < 43:
                    self.humidifier.Turn_On()
                    self.humidifier_state = True
                    log("HUMIDIFIER", self.humidifier_state)
            else:
                if humidity > 47:
                    self.humidifier.Turn_Off()
                    self.humidifier_state = False
                    log("HUMIDIFIER", self.humidifier_state)
            

    def calculate_avg_humidity(self):
        self.avg_humidity = (self.instant_humidity1 + self.instant_humidity2) / 2
    
    def get_average_humidity(self):
        return self.avg_humidity
        
    def get_humidity1(self):
        return self.instant_humidity1
    
    def get_humidity2(self):
        return self.instant_humidity2
        
    def is_max(self, humidity):
        if humidity > self.max_humidity:
            self.max_humidity = humidity
            
    def is_min(self, humidity):
        if humidity < self.min_humidity:
            self.min_humidity = humidity
        
    def get_min_humidity(self):
        return self.min_humidity
        
    def get_max_humidity(self):
        return self.max_humidity
###############################################################################
# File Name  : Shared.py
# Date       : 03/14/2021
# Description: 
###############################################################################

from datetime import datetime
from support import log
from support import div

class Temperature:
    def __init__(self, config):
        self.max_temperature = 0
        self.min_temperature = 99
        self.avg_temperature = 0
        self.config = config
        
    def process_new_data(self, temperature, time):
        # number plausibility check and handle
        # doing stats on good number
        div()
        log("Processing", "Temperature")
        log("Temperature", temperature)
        log("Time", time)
        # self.calculate_avg_humidity()
        # self.is_max(self.avg_humidity)
        # self.is_min(self.avg_humidity)

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

class Humidity:
    def __init__(self, config):
        self.config = config
        self.max_humidity = 0
        self.min_humidity = 99
        self.five_min_avg_humidity = 0
        self.instant_humidity = 0
        #self.instant_time = 
        
    def process_new_data(self, humidity, time):
        # number plausibility check and handle
        # doing stats on good number
        div()
        log("Processing", "Humidity")
        log("Humidity", humidity)
        log("Time", time)
        # self.calculate_avg_humidity()
        # self.is_max(self.avg_humidity)
        # self.is_min(self.avg_humidity)

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
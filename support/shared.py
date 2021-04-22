###############################################################################
# File Name  : Shared.py
# Date       : 03/14/2021
# Description: 
###############################################################################

from datetime import datetime
from support import log
from support import div
from control.heater import Heater
from control.humidifier import Humidifier

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
        div()
        channel = data["name"]
        temperature = data["temp"]
        time = data["time"]
        # self.temperature_data.append(data)
        # log("TempArr", len(self.temperature_data))


        if channel == "ch1":
            if self.heater_state == False:
                if temperature < 70:
                    self.heater.Turn_On()
                    self.heater_state = True
            else:
                if temperature > 75:
                    self.heater.Turn_Off()
                    self.heater_state = False

            log("Processing", "Temperature {}".format(channel))
            log("Temperature", temperature)
            log("Time",time )
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

        if channel == "ch1":
            if self.humidifier_state == False:
                if humidity < 45:
                    self.humidifier.Turn_On()
                    self.humidifier_state = True
            else:
                if humidity > 50:
                    self.humidifier.Turn_Off()
                    self.humidifier_state = False

            log("Processing", "Humidity {}".format(channel))
            log("Humidity", humidity)
            log("Time",time )
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




###############################################################################
# Filename    : room.py
# Date        : 04/10/2021 
# Description : Processes room environment data
###############################################################################

from data.db_app import DataBase_App
from support import log

class Room:
    def __init__(self, config):
        humidity = Humidity(config)
        temperature = Temperature(config)
        the_database = DataBase_App(the_config)

    def process_room(self):
        temperature.process_temperature()
        humidity.process_humidity()


class Humidity:
    def __init__(self, config):
        self.max_humidity = 0
        self.min_humidity = 99
        self.avg_humidity = 0
        self.config = config
        
    def process_humidity(self):
        self.update_to_latest_record()
        self.calculate_avg_humidity()
        self.is_max(self.avg_humidity)
        self.is_min(self.avg_humidity)

    def update_to_latest_record(self):
        self.sensor1_db.update_to_last_record()
        self.instant_humidity1 = self.sensor1_db.get_last_humidity()
        self.sensor2_db.update_to_last_record()
        self.instant_humidity2 = self.sensor2_db.get_last_humidity()

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


class Temperature:
    def __init__(self, config):
        self.max_temperature = 0
        self.min_temperature = 99
        self.avg_temperature = 0
        self.config = config
        
    def process_temperature(self):
        self.update_to_latest_record()
        self.calculate_avg_temperature()
        self.is_max(self.avg_temperature)
        self.is_min(self.avg_temperature)

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
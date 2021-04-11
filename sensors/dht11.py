###############################################################################
# File Name  : DHT11.py
# Date       : 03/14/2021
# Description: Reads humidity sensor
###############################################################################

import Adafruit_DHT
from support.shared import Sensor_Data
from support import log
from datetime import datetime


class DHT11:
    sensor_index = 0
    def __init__(self, config):
        if len(config.dht11_config) > self.sensor_index:
            self.pin = config.dht11_config[self.sensor_index]["pin"]
            self.name = config.dht11_config[self.sensor_index]["name"]
            self.sensor_type = config.dht11_config[self.sensor_index]["sensor_type"]
            self.current_data = Sensor_Data()
            self.current_data.name = config.dht11_config[self.sensor_index]["name"]
            self.retrys = config.sensor_retrys
            DHT11.sensor_index += 1
            self.process_sensor()
            log("Success Processing", "Sensor Started Successfully")
        else:
            log("Error", "All Sensors Used or some other error")
        
    def __del__(self): 
        pass
        
    def process_sensor(self):
        log("Processing", self.name)
        process_start_time = datetime.now()

        try:
            humidity, temperature_c = Adafruit_DHT.read_retry(self.sensor_type, self.pin, self.retrys)
            if humidity is not None and temperature_c is not None:
                temperature_f = temperature_c * 9/5.0 + 32
                self.current_data.time_data = datetime.now()
                self.current_data.temperature_f = temperature_f
                self.current_data.humidity = humidity
                self.current_data.error_state = False
                log("Time", self.current_data.time_data)
                log("Temp", self.current_data.temperature_f)
                log("Humidity", self.current_data.humidity)
                log("Error State", self.current_data.error_state)
            else:
                self.current_data.error_state = True
        except:
            self.current_data.error_state = True
            
        process_end_time = datetime.now()
        log("Process Time", (process_end_time - process_start_time))

    def get_current_data(self):
        return self.current_data
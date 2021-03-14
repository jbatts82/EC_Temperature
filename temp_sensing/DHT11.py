###############################################################################
# File Name  : DHT11.py
# Date       : 03/14/2021
# Description: Reads humidity sensor
###############################################################################

import Adafruit_DHT
from support.shared import DHT11_Data
from datetime import datetime

class DHT11:
    sensor_index = 0
    def __init__(self, config):
        if config.sensor_cnt > self.sensor_index:
            self.pin = config.sensor_configs[self.sensor_index]["data_pin"]
            self.name = config.sensor_configs[self.sensor_index]["name"]
            self.sensor_type = config.sensor_configs[self.sensor_index]["sensor_type"]
            self.current_data = DHT11_Data()
            self.previous_data = DHT11_Data() #ie:previous good data
            self.current_data.name = config.sensor_configs[self.sensor_index]["name"]
            DHT11.sensor_index += 1
            self.process_sensor()
            print("Success Processing : Sensor Started Successfully")
        else:
            print("Error              : All Sensors Used or some other error")
        
    def __del__(self): 
        pass
        
    def process_sensor(self):
        print("Processing         :", self.name)
        process_start_time = datetime.now()
        try:
            humidity, temperature_c = Adafruit_DHT.read_retry(self.sensor_type, self.pin)
            temperature_f = temperature_c * 9/5.0 + 32
            self.current_data.time_data = datetime.now()
            self.current_data.temperature_f = temperature_f
            self.current_data.humidity = humidity
            self.current_data.error_state = False
        except:
            print("!!!SIGNAL SNA!!!   :",self.name)
            self.current_data = self.previous_data
        else:
            print("Success Processing :", self.name)
            print("Time               :", self.current_data.time_data)
            print("Temp               :", self.current_data.temperature_f)
            print("Humidity           :", self.current_data.humidity)
            print("Error State        :", self.current_data.error_state)
            self.previous_data = self.current_data
        finally:
            process_end_time = datetime.now()
            print("Process Time       : {}".format(process_end_time - process_start_time))
    
    def get_current_data(self):
        return self.current_data

#end: class Sensor:
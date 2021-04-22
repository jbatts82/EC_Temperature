###############################################################################
# File Name  : DHT11.py
# Date       : 03/14/2021
# Description: Reads humidity sensor
###############################################################################

import Adafruit_DHT
from support import log
from support import div
from datetime import datetime


class DHT11:
    def __init__(self, config):
        self.pin = config["pin"]
        self.name = config["name"]
        self.sensor_type = config["sensor_type"]
        self.retrys = 5
        self.current_data = None
        
    def process_sensor(self):
        #div()
        log("Processing", self.name)
        process_start_time = datetime.now()
        try:
            humidity, temperature_c = Adafruit_DHT.read_retry(self.sensor_type, self.pin, self.retrys)
            if humidity is not None and temperature_c is not None:
                temperature_f = temperature_c * 9/5.0 + 32
                self.current_data = {"name":self.name, "time": datetime.now(), "temp":temperature_f, "hum":humidity, "err":False}
                # log("Time", self.current_data["time"])
                # log("Temp", self.current_data["temp"])
                # log("Humidity", self.current_data["hum"])
                # log("Error State", self.current_data["err"])
            else:
                self.current_data = {"name":self.name, "time":datetime.now(), "temp":None, "hum":None, "err":True}
        except:
            self.current_data = {"name":self.name, "time":datetime.now(), "temp":None, "hum":None, "err":True}
            
        process_end_time = datetime.now()
        log("Process Time", (process_end_time - process_start_time))

    def get_current_data(self):
        return self.current_data
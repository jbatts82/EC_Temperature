###############################################################################
# File Name  : Shared.py
# Date       : 03/14/2021
# Description: 
###############################################################################

from datetime import datetime

class DHT11_Data:
    def __init__(self, name=None, time_data=0, humidity=0, temperature_f=0):
        self.name = name
        self.time_data = time_data
        self.humidity = humidity
        self.temperature_f = temperature_f
        self.error_state = True

    def print_data(self):
        print("DHT11 Name : ",self.name)
        print("Time       : ",self.time_data)
        print("Humidity   : ",self.humidity)
        print("Temperature: ",self.temperature_f)
        print("Error State: ",self.error_state)

class Control_Data:
    def __init__(self, time_stamp=None, heater_state=None, humidifer_state=None, fan_state=None, light_state=None):
        self.time_stamp = time_stamp
        self.heater_state = heater_state
        self.humidifer_state = humidifer_state
        self.fan_state = fan_state
        self.light_state = light_state

    def print_data(self):
        print("Time Stamp : ",self.time_stamp)
        print("Heater Stat: ",self.heater_state)
        print("Hum Stat   : ",self.humidifer_state)
        print("Fan Stat   : ",self.fan_state)
        print("LED Stat   : ",self.light_state)

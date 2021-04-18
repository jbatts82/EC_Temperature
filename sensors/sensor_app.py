###############################################################################
# File Name  : sensor_app.py
# Date       : 04/10/2021
# Description: 
###############################################################################


from sensors.dht11 import DHT11
from config import Config
from support import log
import data.room_data as rd
from datetime import datetime

the_config = Config()

# initialize temp sensing
sensor1 = DHT11(the_config.dht11_config[0])
sensor2 = DHT11(the_config.dht11_config[1])
sensor3 = DHT11(the_config.dht11_config[2])
sensor4 = DHT11(the_config.dht11_config[3])

sensor_array = [sensor1, sensor2, sensor3, sensor4]

dht_data_array = []

def Process_Sensors():
	global dht_data_array, sensor_array
	for sensor in sensor_array:
		sensor.process_sensor()
		new_data = sensor.get_current_data()
		dht_data_array.append(new_data)

def Get_Sensor_Data():
	global dht_data_array
	return dht_data_array

def print_the_array():
	global dht_data_array
	for ind, each in enumerate(dht_data_array):
		log(str(ind), each["time"])

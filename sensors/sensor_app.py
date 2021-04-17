###############################################################################
# File Name  : sensor_app.py
# Date       : 04/10/2021
# Description: 
###############################################################################

from collections import deque
from sensors.dht11 import DHT11
from support.shared import Sensor_Data
from config import Config
from support import log
import data.room_data as rd
from datetime import datetime

the_config = Config()

# initialize temp sensing
sensor1 = DHT11(the_config)
sensor2 = DHT11(the_config)
sensor3 = DHT11(the_config)
sensor4 = DHT11(the_config)
sensor_array = [sensor1, sensor2, sensor3, sensor4]

dht_data_array = []
count = 0

def Process_Sensors():
	global dht_data_array, sensor_array, count
	count = count + 1
	log("Count", count)
	for sensor in sensor_array:
		print("Processing Sensor")
		sensor.process_sensor()
		dht_data = sensor.get_current_data()
		dht_data_array.append(dht_data)

def print_the_array():
	global dht_data_array
	log("array Length", len(dht_data_array))
	for each in dht_data_array:
		each.print_data()
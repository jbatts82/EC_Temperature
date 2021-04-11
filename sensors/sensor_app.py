###############################################################################
# File Name  : sensor_app.py
# Date       : 04/10/2021
# Description: 
###############################################################################

from sensors.dht11 import DHT11
from support.shared import Sensor_Data

from config import Config

the_config = Config()

# initialize temp sensing
sensor1 = DHT11(the_config)
sensor2 = DHT11(the_config)
sensor3 = DHT11(the_config)
sensor4 = DHT11(the_config)
sensor_array = [sensor1, sensor2, sensor3, sensor4]

dht_data_array = []

def Process_Sensors():
	for idx, sensor in enumerate(sensor_array):
		sensor_array[idx].process_sensor()
		dht_data = sensor_array[idx].get_current_data()
		dht_data_array.append(dht_data)

def Get_Data():
	return dht_data_array

###############################################################################
# File Name  : TheSensorApp.py
# Date       : 03/13/2021
# Description: 
###############################################################################

import asyncio
from time import sleep
from config import Config
from temp_sensing.DHT11 import DHT11
from support import log
from support import div
from data.DB_App import DataBase_App
from control.leds import leds
from control.plug import KasaPlug

if __name__ == '__main__':
	log("Starting Main System", __file__)
	div()
	the_config = Config()

	# initialize database
	div()
	the_database = DataBase_App(the_config)

	# initialize leds
	div()
	the_leds = leds(the_config)

	# initialize temp sensing
	sensor1 = DHT11(the_config)
	sensor2 = DHT11(the_config)
	sensor3 = DHT11(the_config)
	sensor4 = DHT11(the_config)
	sensor_array = [sensor1, sensor2, sensor3, sensor4]


	# Run Sensors
	while True:
		for sensor in sensor_array:
			div()
			sensor.process_sensor()
		sleep(10)
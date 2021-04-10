###############################################################################
# File Name  : TheSensorApp.py
# Date       : 03/13/2021
# Description: 
###############################################################################

import sys
import asyncio
import schedule
import threading
from time import sleep
from config import Config
from sensors.dht11 import DHT11
from support import log
from support import div
from data.room import Room
from control.leds import leds
from control.heater import Heater
from control.fan import Fan








def read_sensor(idx):
	global error_count
	div()
	the_leds.turn_on(idx)
	sensor_array[idx].process_sensor()
	current_data = sensor_array[idx].get_current_data()
	result = plausiblity_check(current_data)
	if result == True: #clean
		the_database.write_sensor_data(current_data)
		log("DB Status", "Saved to database")
		sleep(1)
	else:
		error_count = error_count + 1
	the_leds.turn_off(idx)

def read_all_sensors(sensor_array):
	#do error checking and reporting
	for idx, sensor in enumerate(sensor_array):
		div()
		read_sensor(idx)

if __name__ == '__main__':
	log("Starting Main System", __file__)
	div()
	
	the_config = Config()
	error_count = 0

	# initialize leds
	div()
	the_leds = leds(the_config)

	# initialize temp sensing
	sensor1 = DHT11(the_config)
	sensor2 = DHT11(the_config)
	sensor3 = DHT11(the_config)
	sensor4 = DHT11(the_config)
	sensor_array = [sensor1, sensor2, sensor3, sensor4]

	# initalize control objects
	the_heater = Heater(the_config)
	the_fan = Fan(the_config)
	the_room = Room(the_config)




	# schedule tasks
	schedule.every().minute.at(":00").do(read_all_sensors, sensor_array)
	schedule.every().minute.at(":15").do(read_all_sensors, sensor_array)
	schedule.every().minute.at(":30").do(read_all_sensors, sensor_array)
	schedule.every().minute.at(":45").do(read_all_sensors, sensor_array)






	# main loop
	try:
		while True: #run forever
			schedule.run_pending()
			sleep(1)
	except KeyboardInterrupt:
		print("---You Killed me.")
	except:
		print("System Error")
		print("Unexpected error:", sys.exc_info()[0])
		raise
	finally:
		the_heater.Kill()
		print("bye..bye")
		sys.exit(0)
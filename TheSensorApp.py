###############################################################################
# File Name  : TheSensorApp.py
# Date       : 03/13/2021
# Description: 
###############################################################################

from config import Config
from temp_sensing.DHT11 import DHT11
from support import log
import asyncio
from time import sleep

from data.DB_App import DataBase_App


if __name__ == '__main__':
	log("Starting", __file__)
	
	the_config = Config()
	the_database = DataBase_App(the_config)

	sensor1 = DHT11(the_config)
	sensor1.process_sensor()
	sensor_data = sensor1.get_current_data()

	the_database.write_sensor_data(sensor_data)




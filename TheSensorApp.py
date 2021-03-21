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
from data.DB_App import DataBase_App
from control.leds import leds
from control.plug import KasaPlug

if __name__ == '__main__':
	print("###############################################################################")
	log("Starting Main System", __file__)
	
	the_config = Config()

	# initialize database
	print("###############################################################################")
	the_database = DataBase_App(the_config)

	# initialize leds
	print("###############################################################################")
	the_leds = leds(the_config)

	# initialize temp sensing
	print("###############################################################################")
	sensor1 = DHT11(the_config)
	print("###############################################################################")
	sensor2 = DHT11(the_config)
	print("###############################################################################")
	sensor3 = DHT11(the_config)
	print("###############################################################################")
	sensor4 = DHT11(the_config)

	# initialize plug controlers
	print("###############################################################################")
	plug1 = KasaPlug(the_config)
	print("###############################################################################")
	plug2 = KasaPlug(the_config)
	print("###############################################################################")
	plug3 = KasaPlug(the_config)
	print("###############################################################################")
	plug4 = KasaPlug(the_config)
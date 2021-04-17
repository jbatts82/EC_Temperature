###############################################################################
# File Name  : TheSensorApp.py
# Date       : 03/13/2021
# Description: 
###############################################################################

import sys
import asyncio
import schedule
import sensors.sensor_app as sa
from time import sleep
from config import Config
from support import log
from support import div
import data.room_data as rd
from datetime import datetime
import data.room_data as rd
from control.leds import Leds
from support.shared import Sensor_Data


if __name__ == '__main__':
	log("Starting Main System", __file__)
	the_config = Config()

	count = 0

	# main loop
	try:
		while True: #run forever
			count = count + 1
			schedule.run_pending()
			the_leds.toggle(7)
			sleep(1)
	except KeyboardInterrupt:
		print("---You Killed me.")
	except:
		print("System Error")
		print("Unexpected error:", sys.exc_info()[0])
		raise
	finally:
		print("bye..bye")
		sys.exit(0)
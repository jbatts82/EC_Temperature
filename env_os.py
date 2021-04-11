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

from data.room_data import RoomData
from control.leds import Leds


if __name__ == '__main__':
	log("Starting Main System", __file__)
	the_config = Config()

	# initialize leds
	the_leds = Leds(the_config)

	# initalize control objects
	room_data = RoomData(the_config)

	
	# schedule tasks
	schedule.every().minute.at(":00").do(sa.Process_Sensors)
	schedule.every().minute.at(":15").do(sa.Process_Sensors)
	schedule.every().minute.at(":30").do(sa.Process_Sensors)
	schedule.every().minute.at(":45").do(sa.Process_Sensors)


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
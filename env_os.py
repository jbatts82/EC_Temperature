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
from control.leds import Leds


if __name__ == '__main__':
	log("Starting System", __file__)
	the_config = Config()

	the_leds = Leds(the_config)
	rd.Init_Room(the_config)


	schedule.every(15).seconds.do(sa.Process_Sensors)
	schedule.every(60).seconds.do(rd.Process_Room)


	# main loop
	try:
		while True: #run forever
			schedule.run_pending()
			the_leds.toggle(7)
			sleep(1)
	except Exception as e:
		print("EXCEPTION", str(e))
	except KeyboardInterrupt:
		print("---You Killed me.")
	except:
		print("System Error")
		print("Unexpected error:", sys.exc_info()[0])
		raise
	finally:
		print("bye..bye")
		sys.exit(0)
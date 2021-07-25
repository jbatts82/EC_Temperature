###############################################################################
# File Name  : TheSensorApp.py
# Date       : 03/13/2021
# Description: 
###############################################################################

import sys
import asyncio
import schedule
import sensors.sensor_app as sa
import control.room_control as rc
import keyboard
from time import sleep
from config import Config
from support import log
from support import div
from support.timeclock import OS_Clock
import data.room_data as rd
import data.db_app as db
from datetime import datetime
from control.leds import Leds
import traceback


if __name__ == '__main__':
	log("Starting System", __file__)

	the_config = Config()
	system_clock = OS_Clock()
	db.Db_App_Init(the_config)
	the_leds = Leds(the_config)
	rd.Init_Room_Data(the_config)
	rc.Init_Room_Control(the_config)

	schedule.every(15).seconds.do(sa.Process_Sensors)
	schedule.every(30).seconds.do(rd.Process_Room_Data)
	schedule.every(60).seconds.do(rc.Process_Room_Control, system_clock)

	schedule.every().hour.at(":00").do(rc.Request_Fan_On, "periodic")
	schedule.every().hour.at(":30").do(rc.Request_Fan_On, "periodic")


	# main loop
	try:
		while True: #run forever
			schedule.run_pending()
			the_leds.toggle(7)
			sleep(1)
	except KeyboardInterrupt:
		print("---You Killed me.")
	except:
		print("System Error")
		print("Unexpected error: ", sys.exc_info())
		print("Trackback: ", traceback.format_exc())
		raise
	finally:
		rc.Kill_Everything()
		print("bye..bye")
		sys.exit(0)
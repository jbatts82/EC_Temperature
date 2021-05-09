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
from time import sleep
from config import Config
from support import log
from support import div
from support.timeclock import OS_Clock
import data.room_data as rd
import data.db_app as db
from datetime import datetime
from control.leds import Leds


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

	schedule.every().day.at("01:15").do(rc.Request_Fan_On, "periodic")
	schedule.every().day.at("03:15").do(rc.Request_Fan_On, "periodic")
	schedule.every().day.at("05:15").do(rc.Request_Fan_On, "periodic")
	schedule.every().day.at("07:15").do(rc.Request_Fan_On, "periodic")
	schedule.every().day.at("09:15").do(rc.Request_Fan_On, "periodic")
	schedule.every().day.at("11:15").do(rc.Request_Fan_On, "periodic")
	schedule.every().day.at("13:15").do(rc.Request_Fan_On, "periodic")
	schedule.every().day.at("15:15").do(rc.Request_Fan_On, "periodic")
	schedule.every().day.at("17:15").do(rc.Request_Fan_On, "periodic")
	schedule.every().day.at("19:15").do(rc.Request_Fan_On, "periodic")
	schedule.every().day.at("21:15").do(rc.Request_Fan_On, "periodic")
	schedule.every().day.at("23:15").do(rc.Request_Fan_On, "periodic")

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
		rc.Kill_Everything()
		print("bye..bye")
		sys.exit(0)
###############################################################################
# File Name  : web_control.py
# Date       : 08/06/2021
# Description: handles web requests to control room
###############################################################################

from support import log, div
import data.db_app as db
from datetime import datetime

def Init_WebControl():
	db.Init_Data_Control_Table()


def Update_Web_Control_Table(req_data):
	log("req_data", str(req_data))

	time_stamp = datetime.now()

	heater_req = req_data["heater_req"]
	heater_state = req_data["heater_state"]

	humidifier_req = req_data["humidifier_req"]
	humidifier_state = req_data["humidifier_req"]

	fan_req = req_data["fan_req"]
	fan_state = req_data["fan_state"]

	light_req = req_data["light_req"]
	light_state = req_data["light_state"]

	db.Write_Web_Control_Request(time_stamp, heater_req, heater_state, \
		humidifier_req, humidifier_state, fan_req, fan_state, light_req, light_state)
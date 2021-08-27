###############################################################################
# File Name  : models.py
# Date       : 08/25/2020
# Description: P
###############################################################################


from support import log, div
import data.db_app as db
from datetime import datetime


The_Model = {
	"graph_lines": {"ch1": True, "ch2": False, "ch3": False, "ch4": False, "heater": False, "light": True, "fan": False},

	"web_control": {
					"heater_req": False,
					"heater_state": False,
					"fan_req": False,
					"fan_state": False, }
}


def Init_WebControl():
	db.Init_Data_Control_Table()

def update_client_model(client_model):
	The_Model = client_model
	log("WebControll", The_Model)

def get_model():
	return The_Model

def Update_Web_Control_Table(req_data):
	log("req_data", str(req_data))

	time_stamp = datetime.now()

	heater_req = req_data["heater_req"]
	heater_state = req_data["heater_state"]

	fan_req = req_data["fan_req"]
	fan_state = req_data["fan_state"]


	db.Write_Web_Control_Request(time_stamp, heater_req, heater_state, fan_req, fan_state)
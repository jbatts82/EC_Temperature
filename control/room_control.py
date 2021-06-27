###############################################################################
# Filename    : room_control.py
# Date        : 04/10/2021 
# Description : Processes room environment data
###############################################################################

from control.humidifier import Humidifier
from control.heater import Heater
from control.fan import Fan
from control.lamp import Lamp
from datetime import datetime
from support import log
from support import div
import data.db_app as db

heater_state = None
humidifier_state = None
heater = None
humidifier = None
fan = None
timer = 0

heater_request_list = {
	"temperature":False
}

humidity_request_list = {
	"humidity":False
}

exhaust_request_list = {
	"temperature":False,
	"humidity":False,
	"periodic":False
}

def Init_Room_Control(the_config):
	global heater, humidifier, fan, lamp
	log("Room Control", "Init")
	heater = Heater(the_config)
	humidifier = Humidifier(the_config)
	fan = Fan(the_config)
	lamp = Lamp(the_config)
	
def Process_Room_Control(clock):
	global heater, humidifier, fan, lamp, heater_request_list, \
	humidity_request_list, exhaust_request_list

	log("Processing", "Room Control On Time: {}".format(clock.get_time_since_start()))

	process_heater_requests(heater_request_list)
	process_humidifier_requests(humidity_request_list)
	process_fan_requests(exhaust_request_list)
	
	lamp.Process_Lamp()
	heater.Process_Heater()
	humidifier.Process_Humidifier()
	fan.Process_Fan()

	log("Time", clock.get_current_time_stamp())
	log("Heater State", heater.Get_State())
	log("Humidifier State", humidifier.Get_State())
	log("Fan State", fan.Get_State())
	log("Lamp State", lamp.Get_State())

	db.Write_Control_Data(clock.get_current_time_stamp(), heater.Get_State(), humidifier.Get_State(), fan.Get_State(), lamp.Get_State())

def Request_Heater_On(requester):
	global heater_request_list
	heater_request_list[requester] = True

def Request_Heater_Off(requester):
	global heater_request_list
	heater_request_list[requester] = False

def Request_Humidifier_On(requester):
	global humidity_request_list
	humidity_request_list[requester] = True

def Request_Humidifier_Off(requester):
	global humidity_request_list
	humidity_request_list[requester] = False

def Request_Fan_On(requester):
	global exhaust_request_list
	exhaust_request_list[requester] = True

def Request_Fan_Off(requester):
	global exhaust_request_list
	exhaust_request_list[requester] = False

def Kill_Everything():
	global heater, humidifier
	heater.Turn_Off()
	humidifier.Turn_Off()
	fan.Turn_Off()

def process_heater_requests(requests):
	global heater, fan
	on_req = 0
	for req in requests.values():
		if req == True:
			on_req = on_req + 1

	if fan.Get_State == True:
		return

	if on_req == 0:
		heater.Turn_Off()
	else:
		heater.Turn_On()

def process_humidifier_requests(requests):
	global humidifier
	on_req = 0
	for req in requests.values():
		if req == True:
			on_req = on_req + 1

	if fan.Get_State == True:
		return

	if on_req == 0:
		humidifier.Turn_Off()
	else:
		humidifier.Turn_On()

def process_fan_requests(requests):
	global fan
	on_req = 0
	for req in requests.keys():
		if requests[req] == True:
			if req == "periodic":
				fan.Set_Fan_Timer(45)
				requests[req] = False

	fan.Process_Fan()
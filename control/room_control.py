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
from support import log, div
import data.db_app as db
from support.timeclock import Device_Clock

heater_state = None
humidifier_state = None
heater = None
humidifier = None
fan = None
timer = 0
fan_on_time = 15
last_time = False
periodic_init = True


heater_request_list = {
	"temperature":False,
	"web_override":False,
	"web_state":False,
}

humidity_request_list = {
	"humidity":False,
	"web_override":False,
	"web_state":False,
}

exhaust_request_list = {
	"temperature":False,
	"humidity":False,
	"periodic":False,
	"override":False,
	"web_override":False,
	"web_state":False,
}

def Init_Room_Control(the_config):
	global heater, humidifier, fan, lamp
	log("Room Control", "Init")
	heater = Heater(the_config)
	humidifier = Humidifier(the_config)
	fan = Fan(the_config)
	lamp = Lamp(the_config)
	
	
def Process_Room_Control(clock):
	log("Processing", "Room Control On Time: {}".format(clock.get_time_since_start()))
	global heater, humidifier, fan, lamp, heater_request_list, \
	humidity_request_list, exhaust_request_list


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

def process_web_requests():
	global last_time

	web_control_req = db.Get_Last_Web_Control_Rec()

	time_stamp = web_control_req.time_stamp

	if time_stamp == last_time:
		return


	exhaust_request_list["web_override"] = web_control_req.fan_req
	exhaust_request_list["web_state"] = web_control_req.fan_state

	heater_request_list["web_override"] = web_control_req.heater_req
	heater_request_list["web_override"] = web_control_req.heater_state

	humidifier_state = web_control_req.humidifier_state
	light_req = web_control_req.light_req
	light_state = web_control_req.light_state

	last_time = time_stamp


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
	global fan, fan_on_time, fan_timer, periodic_init

	if requests["web_override"]:
		if requests["web_state"]:
			fan.Turn_On()
		else:
			fan.Turn_Off()
		return

	if requests["periodic"]:
		if periodic_init:
			fan_timer = Device_Clock()
			fan_timer.set_on_timer(10)
			fan.Turn_On()
			periodic_init = False
		else:
			is_timer_on = fan_timer.process_clock() 
			if not is_timer_on:
				fan.Turn_Off()
				requests["periodic"] = False
				periodic_init = True
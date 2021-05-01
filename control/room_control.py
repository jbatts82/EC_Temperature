###############################################################################
# Filename    : room_control.py
# Date        : 04/10/2021 
# Description : Processes room environment data
###############################################################################

from control.humidifier import Humidifier
from control.heater import Heater
from datetime import datetime
from support import log
from support import div

heater_state = None
humidifier_state = None
heater = None
humidifier = None

def Init_Room_Control(the_config):
	global heater, humidifier
	log("Room Control", "Init")
	heater = Heater(the_config)
	humidifier = Humidifier(the_config)
	
def Process_Room_Control():
	global heater
	log("Processing", "Room Control")
	log("Heater State", heater.Get_State())
	
def Request_Heater_On():
	global heater
	heater.Turn_On()

def Request_Heater_Off():
	global heater
	heater.Turn_Off()

def Request_Humidifier_On():
	global humidifier
	humidifier.Turn_On()

def Request_Humidifier_Off():
	global humidifier
	humidifier.Turn_Off()

def Kill_Everything():
	global heater, humidifier
	heater.Turn_Off()
	humidifier.Turn_Off()
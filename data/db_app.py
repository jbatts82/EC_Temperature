###############################################################################
# File Name  : DB_App.py
# Date       : 03/18/2021
# Description: Database Application Layer 
###############################################################################

import data.db_handler as db_hand
from data.db_handler import Instant_Temperature
from data.db_handler import Instant_Humidity
from data.db_handler import Instant_Sensor
from data.db_handler import Control_Status, Web_Control_Request
from support import log
from support import div
from time import sleep
from datetime import datetime
import WebApp.models as wc



def Db_App_Init(the_config):
	db_hand.init_database_engine(the_config)
	wc.Init_WebControl()


def Write_Temp_Sensor_Data(time, channel, temp_f, hum):
	reading = Instant_Sensor()
	reading.time_stamp = time
	reading.channel = channel
	reading.temperature = temp_f
	reading.humidity = hum
	db_hand.insert_instant_sensor(reading)


def Write_Instant_Temp(time, channel, temp_f):
	reading = Instant_Temperature()
	reading.time_stamp = time
	reading.channel = channel
	reading.temperature = temp_f
	db_hand.insert_instant_temp(reading)


def Write_Instant_Humidity(time, channel, hum):
	reading = Instant_Humidity()
	reading.time_stamp = time
	reading.channel = channel
	reading.humidity = hum
	db_hand.insert_instant_hum(reading)


def Write_Control_Data(time_stamp, heater_state, humidifier_state, fan_state, light_state):
	control_stats = Control_Status()
	control_stats.time_stamp = time_stamp
	control_stats.heater_state = heater_state
	control_stats.humidifier_state = humidifier_state
	control_stats.fan_state = fan_state
	control_stats.light_state = light_state
	db_hand.insert_control_record(control_stats)


def Write_Web_Control_Request(time_stamp, heater_req, heater_state, \
	humidifier_req, humidifier_state, fan_req, fan_state, light_req, light_state):
	web_control = Web_Control_Request()
	web_control.time_stamp = time_stamp

	web_control.heater_req = heater_req
	web_control.heater_state = heater_state

	web_control.humidifier_req = humidifier_req
	web_control.humidifier_state = humidifier_state

	web_control.fan_req = fan_req
	web_control.fan_state = fan_state

	web_control.light_req = light_req
	web_control.light_state = light_state

	db_hand.insert_web_control_record(web_control)


def Get_Last_Web_Control_Rec():
	record = db_hand.get_web_control_recrd()
	return record


def Get_Last_Sensor_Rec(channel):
	record = db_hand.get_last_sensor_rec(channel)
	return record


def Get_Last_Sensor_List(channel, time):
	records = db_hand.get_last_sensor_list(channel, time)
	return records


def Get_Last_Temp_Rec(channel):
	record = db_hand.get_last_temp_rec(channel)
	last_temperature = record.temperature
	last_time = record.time_stamp
	return last_temperature, last_time


def Get_Last_Temp_List(channel, time):
	records = db_hand.get_last_temp_list(channel, time)
	return records


def Get_Last_Humid_Rec(channel):
	record = db_hand.get_last_humid_rec(channel)
	last_humid = record.humidity
	last_time = record.time_stamp
	return last_humid, last_time


def Get_Last_Humid_List(channel, time):
	records = db_hand.get_last_humid_list(channel, time)
	return records


def Get_Last_Control_Rec():
	record = db_hand.get_last_control_rec()
	return record


def Get_Last_Control_List(time):
	records = db_hand.get_last_control_list(time)
	return records


def Delete_Table(table_class):
	db_hand.delete_table(table_class)


def Init_Data_Control_Table():
	if db_hand.table_exists(Web_Control_Request):
		Delete_Table(Web_Control_Request)
		Write_Web_Control_Request(datetime.now(), False, False, False, False, False, False, False, False)
	else:
		Write_Web_Control_Request(datetime.now(), False, False, False, False, False, False, False, False)
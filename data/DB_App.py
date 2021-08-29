###############################################################################
# File Name  : DB_App.py
# Date       : 03/18/2021
# Description: Database Application Layer 
###############################################################################

import data.db_handler as db_hand
from data.db_handler import Instant_Temperature
from data.db_handler import Instant_Humidity
from data.db_handler import Instant_Sensor
from data.db_handler import Control_Status, Web_Model
from support import log
from support import div
from time import sleep
from datetime import datetime
import WebApp.models as wc
import json



def Db_App_Init(the_config):
	db_hand.init_database_engine(the_config)


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
	

def Write_Web_Model_Rec(time_stamp, model):
	web_model = Web_Model()
	web_model.time_stamp = time_stamp
	jsonData = json.dumps(model)
	web_model.the_model = jsonData
	db_hand.insert_model_record(web_model)


def Get_Web_Model_Rec():
	record = db_hand.get_model_recrd()
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


def Init_Web_Model():
	# if db_hand.table_exists(Web_Model):
	# 	log("DB", "Table Exisits")
	# 	return
	# log("DB", "Init Model Rec")
	# time_stamp = datetime.now()
	# model = wc.get_ram_model()
	# Write_Model_Record(time_stamp, model)
	pass
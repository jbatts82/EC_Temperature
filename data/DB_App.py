###############################################################################
# File Name  : DB_App.py
# Date       : 03/18/2021
# Description: Database Application Layer 
###############################################################################

import data.db_handler as db_hand
from data.db_handler import Instant_Temperature
from data.db_handler import Instant_Humidity
from support import log
from support import div


def Db_App_Init(the_config):
	db_hand.Init_Database_Engine(the_config)

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
	reading.temperature = hum
	db_hand.insert_instant_hum(reading)


def Dump_Instant_Temp():
	db_hand.dump_table()

# def write_control_data(self, time_stamp, heater_state, humidifier_state, fan_state, light_state):
# 	control_stats = ControlStatus()
# 	control_stats.time_stamp = time_stamp
# 	control_stats.heater_state = heater_state
# 	control_stats.humidifier_state = humidifier_state
# 	control_stats.fan_state = fan_state
# 	control_stats.light_state = light_state
# 	self.control_base.insert_record(control_stats)

# def get_last_sensor_reading(self):
# 	last_rec = self.data_base.get_last_sensor_rec()
# 	sensor_data = DHT11_Data()
# 	sensor_data.name = last_rec.sensor
# 	sensor_data.time_data = last_rec.time_stamp
# 	sensor_data.temperature_f = last_rec.temperature
# 	sensor_data.humidity = last_rec.humidity
# 	return sensor_data

# def get_last_temp(self, sensor_name):
# 	record = self.data_base.get_last_sensor_rec_from(sensor_name)
# 	last_temperature = record.temperature
# 	return last_temperature

# def get_last_humid(self, sensor_name):
# 	record = self.data_base.get_last_sensor_rec_from(sensor_name)
# 	last_humid = record.humidity
# 	return last_humid

# def get_last_avg_room_temp(self):
# 	sensor1_temp = self.get_last_temp("plant1")
# 	sensor2_temp = self.get_last_temp("plant2")
# 	avg_temp = (sensor1_temp + sensor2_temp) / 2
# 	return avg_temp

# def get_last_avg_room_humid(self):
# 	sensor1_temp = self.get_last_humid("plant1")
# 	sensor2_temp = self.get_last_humid("plant2")
# 	avg_humid = (sensor1_temp + sensor2_temp) / 2
# 	return avg_humid

# def dump_sensor_records(self):
# 	self.data_base.dump_table()

# def print_record(self, record):
# 	print("Sensor Name: {}".format(record.sensor))
# 	print("Time       : {}".format(record.time_stamp))
# 	print("Temperature: {}".format(record.temperature))
# 	print("Humidity   : {}".format(record.humidity))
# 	print("")

# def get_previous_readings_time(self, mins_previous, sensor_name):
# 	data = self.data_base.get_last_recs_time(mins_previous, sensor_name)
# 	return data

# def get_previous_control_stats(self, mins_previous):
# 	data = self.control_base.get_last_records(mins_previous)
# 	return data

# def verify_sensor_data(self, sensor_data):
# 	sensor_name = sensor_data.name
# 	sensor_temp = sensor_data.temperature_f
# 	rolling_average_temp = self.get_rolling_avg_temp(sensor_name)

# 	if rolling_average_temp == False:
# 		return True

# 	difference = abs((sensor_temp - rolling_average_temp))

# 	if difference > 10:
# 		return False
# 	else:
# 		return True

# def get_rolling_avg_temp(self, sensor_name):
	
# 	data = self.data_base.get_last_recs_time(5, sensor_name)
	
# 	count = 0
# 	t_sum = 0

# 	for record in data:
# 		if record.sensor == sensor_name:
# 			count = count + 1
# 			t_sum = t_sum + record.temperature

# 	if count == 0:
# 		return False
# 	else:
# 		rolling_average = t_sum / count
# 		return rolling_average
###############################################################################
# Filename    : room_data.py
# Date        : 04/10/2021 
# Description : Processes room environment data
###############################################################################

from support import log
from support import div
import data.temperature as temp
from data.humidity import Humidity
from datetime import datetime
import sensors.sensor_app as sa
import data.db_app as db

error = {}
config = None
humidity =  None
temperature =  None
last_good_reading = None

def Init_Room_Data(the_config):
    global humidity, temperature, error, config
    config = the_config
    humidity = Humidity(config)
    temperature = temp.Init_Temperature(config)

    for sensor_num in range(0, len(config.dht11_config)):
        name = config.dht11_config[sensor_num]["name"]
        error[name] = 0

def Process_Room_Data():
    global humidity, temperature, error
    new_data = sa.Get_Sensor_Data()
    # sensor hw error checks and handle
    for data in new_data:
        channel = data["name"]
        # plausible check
        if data["err"] == True:
            error[channel] = error[channel] + 1
        else:
            db.Write_Temp_Sensor_Data(data["time"], data["name"], data["temp"], data["hum"])
            temp.Process_Temperature(data)
            humidity.process_new_data(data)
    new_data.clear()


def get_last_temp(sensor):
    return 69

def get_error_count(channel):
    return error[channel] 

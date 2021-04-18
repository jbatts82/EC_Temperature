###############################################################################
# Filename    : room_data.py
# Date        : 04/10/2021 
# Description : Processes room environment data
###############################################################################

from data.db_app import DataBase_App
from support import log
from support import div
from support.shared import Temperature
from support.shared import Humidity
from datetime import datetime
import sensors.sensor_app as sa

error = {}
config = None
humidity =  None
temperature =  None


def Init_Room(the_config):
    global humidity, temperature, error
    config = the_config
    humidity = Humidity(config)
    temperature = Temperature(config)

    for sensor_num in range(0, len(config.dht11_config)):
        name = config.dht11_config[sensor_num]["name"]
        error[name] = 0

def Process_Room():
    global humidity, temperature, error
    div()
    log("Processing", "Room")
    new_data = sa.Get_Sensor_Data()

    # sensor hw error checks and handle
    for data in new_data:
        channel = data["name"]
        if data["err"] == True:
            error[channel] = error[channel] + 1
        else:
            humidity.process_new_data(data["hum"], data["time"])
            temperature.process_new_data(data["hum"], data["time"])
        log("Error Count {}".format(channel), error[channel])
    new_data.clear()



# Helper Functions

def plausiblity_check(current_data):

    if current_data.error_state == True:
        return None

    if current_data.temperature_f > the_config.plausible_high:
        return False

    if current_data.temperature_f < the_config.plausible_low:
        return False

    global last_good_reading
    if last_good_reading == None: 
        last_good_reading = current_data
        return True

    difference_f = abs(current_data.temperature_f - last_good_reading.temperature_f)
    if difference_f > the_config.plausible_degrees:
        return False
    last_good_reading = current_data

    return True
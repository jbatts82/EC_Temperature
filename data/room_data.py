###############################################################################
# Filename    : room_data.py
# Date        : 04/10/2021 
# Description : Processes room environment data
###############################################################################

from data.db_app import DataBase_App
from support import log
from support.shared import Temperature
from support.shared import Humidity
from datetime import datetime
from support.shared import Sensor_Data
error = []
config = None
humidity =  None
temperature =  None


def init_room(the_config):
    config = the_config
    humidity = Humidity(config)
    temperature = Temperature(config)
    for sensor_num in range(0, len(config.dht11_config)):
        error.append(0)
        
def process_room(new_data):
    log("DataArr Af", "boo")
    # sensor hw error checks and handle
    for sensor_num, data in enumerate(new_data):
        log("ProcRoomData", data)
        if data.error_state == True:
            error[sensor_num] = error[sensor_num] + 1
            log("Error COunt", error[sensor_num])
        else:
            humidity.process_new_data(data.humidity, data.time_data)
            #temperature.process_new_data(data.temperature, data.time_data)
    new_data.clear()
    log("process_room", "clear data")










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
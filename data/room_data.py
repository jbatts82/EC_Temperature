###############################################################################
# Filename    : room_data.py
# Date        : 04/10/2021 
# Description : Processes room environment data
###############################################################################

from support import log
from support import div
from data.temperature import Temperature
from data.humidity import Humidity
from datetime import datetime
import sensors.sensor_app as sa

error = {}
config = None
humidity =  None
temperature =  None
last_good_reading = None

def Init_Room_Data(the_config):
    global humidity, temperature, error, config
    config = the_config
    humidity = Humidity(config)
    temperature = Temperature(config)

    for sensor_num in range(0, len(config.dht11_config)):
        name = config.dht11_config[sensor_num]["name"]
        error[name] = 0


def Process_Room_Data():
    global humidity, temperature, error
    log("Processing", "Room Data")
    new_data = sa.Get_Sensor_Data()

    # sensor hw error checks and handle
    for data in new_data:
        channel = data["name"]
        if data["err"] == True:
            error[channel] = error[channel] + 1
            log("ERROR", "Not Plausible")
        else:
            # do temperature plausibility check here
            # dont process if bad
            is_plausible = plausiblity_check(data)
            if is_plausible:
                temperature.process_new_data(data)
                humidity.process_new_data(data)
            else:
                error[channel] = error[channel] + 1
                log("ERROR", "Not Plausible")

        log("Error Count {}".format(channel), error[channel])
    new_data.clear()

def get_error_count(channel):
    return error[channel] 

def plausiblity_check(data):
    global config
    if data["temp"] > config.plausible_high:
        return False
    if data["temp"] < config.plausible_low:
        return False

    return True

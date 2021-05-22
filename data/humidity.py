###############################################################################
# File Name  : humidity.py
# Date       : 04/24/2021
# Description: Humidity Data
###############################################################################

import control.room_control as rc
import data.db_app as db
from datetime import datetime
from support import log
from support import div


class Humidity:
    def __init__(self, config):
        self.config = config
        self.max_humidity = 0
        self.min_humidity = 99
        self.five_min_avg_humidity = 0
        self.instant_humidity = 0
        self.humidifier_state = False

    def process_new_data(self, data):
        channel = data["name"]
        humidity = data["hum"]
        time = data["time"]
        #db.Write_Instant_Humidity(time, channel, humidity)
        
        if channel == "ch1":
            #log("Process {} ".format(channel), "Time: {} Hum: {}".format(time, humidity))
            if self.humidifier_state == False:
                if humidity < 43:
                    rc.Request_Humidifier_On("humidity")
                    self.humidifier_state = True
                    log("!!!HUMIDIFIER!!!", self.humidifier_state) 
            else:
                if humidity > 47:
                    rc.Request_Humidifier_Off("humidity")
                    self.humidifier_state = False
                    log("!!!HUMIDIFIER!!!", self.humidifier_state)
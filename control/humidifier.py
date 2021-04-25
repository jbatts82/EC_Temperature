###############################################################################
# File Name  : humidifier.py
# Date       : 04/07/2021
# Description: Humidity Controls
###############################################################################

from time import sleep
from control.plug import KasaPlug
from support import log

class Humidifier:
    def __init__(self, config):
        self.name = "humidifier"
        self.state = False
        hum_config = next(item for item in config.plug_config if item["name"] == "humidifier")
        self.switch = KasaPlug(hum_config)
        self.Turn_Off()

    def Turn_On(self):
        self.state = True
        self.switch.set_plug_on()
        log("Humidifier", "On")
        
    def Turn_Off(self):
        self.state = False
        self.switch.set_plug_off()
        log("Humidifier","Off")
    
    def Get_Name(self):
        return self.name

    def Get_State(self):
        return self.state
        
    def Kill(self):
        self.Turn_Off()
        print("Heater Killed")
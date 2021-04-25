###############################################################################
# File Name  : Heater.py
# Date       : 04/07/2021
# Description: Heater Controls
###############################################################################

from time import sleep
from control.plug import KasaPlug
from support import log

class Heater:
    def __init__(self, config):
        self.name = "heater"
        self.state = False
        heater_config = next(item for item in config.plug_config if item["name"] == "heater")
        self.switch = KasaPlug(heater_config)
        self.Turn_Off()

    def Turn_On(self):
        self.state = True
        self.switch.set_plug_on()
        log("Heater", "On")
        
    def Turn_Off(self):
        self.state = False
        self.switch.set_plug_off()
        log("Heater", "Off")
    
    def Get_Name(self):
        return self.name

    def Get_State(self):
        return self.state
        
    def Kill(self):
        self.Turn_Off()
        print("Heater Killed")
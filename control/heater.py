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
        self.name = "Space Heater"
        self.state = False
        self.switch = KasaPlug(config)
        self.Turn_Off()

    def Turn_On(self):
        self.state = True
        self.switch.set_plug_on()
        log("Heater", "on")
        
    def Turn_Off(self):
        self.state = False
        self.switch.set_plug_off()
        log("Heater", "off")
    
    def Get_Name(self):
        return self.name

    def Get_State(self):
        return self.state
        
    def Kill(self):
        print("Heater Killed")
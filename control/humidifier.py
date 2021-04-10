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
        self.name = "Space Heater"
        self.state = False
        self.switch = KasaPlug(config)

    def Turn_On(self):
        self.state = True
        self.switch.set_plug_on()
        print("on")
        
    def Turn_Off(self):
        self.state = False
        self.switch.set_plug_off()
        print("off")
    
    def Get_Name(self):
        return self.name

    def Get_State(self):
        return self.state
        
    def Kill(self):
        print("Heater Killed")
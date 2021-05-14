###############################################################################
# Filename    : lamp.py
# Date        : 05/09/2021 
# Description : Controls Lamp, light source
###############################################################################

from control.plug import KasaPlug
from support.timeclock import Device_Clock
from support import log

class Lamp:
    def __init__(self, config):
        self.name = "LED Lamp"
        self.state = False
        self.lamp_config = next(item for item in config.plug_config if item["name"] == "lamp")
        self.switch = KasaPlug(self.lamp_config)
        
    def Turn_On(self):
        self.switch.set_plug_on()
        log("Lamp", "On")
    
    def Turn_Off(self):
        self.switch.set_plug_off()
        log("Lamp", "Off")
    
    def Get_Name(self):
        return self.name

    def Get_State(self):
        return self.state

    def Process_Lamp(self):
    	error = self.switch.plug_update()
    	if not error:
    		self.state = self.switch.get_is_on()



     

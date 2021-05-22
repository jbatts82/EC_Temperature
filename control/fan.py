###############################################################################
# Filename    : fan.py
# Date        : 04/09/2021 
# Description : Controls Exhaust Fan
###############################################################################

from time import sleep
from control.plug import KasaPlug
from support.timeclock import Device_Clock
from support import log

class Fan:
    def __init__(self, config):
        self.name = "Exhaust Fan"
        self.state = False
        self.mode = "Auto"
        self.previous_state = False
        self.device_clock = Device_Clock()
        fan_config = next(item for item in config.plug_config if item["name"] == "exhaust")
        self.switch = KasaPlug(fan_config)
        self.Process_Fan()

    def Process_Fan(self):
        error = self.switch.plug_update()
        if not error:
            self.state = self.switch.get_is_on()

    def Turn_On(self):
        self.switch.set_plug_on()
        log("Exhaust Fan", "On")
    
    def Turn_Off(self):
        self.switch.set_plug_off()
        log("Exhaust Fan", "Off")
    
    def Get_Name(self):
        return self.name

    def Get_State(self):
        return self.state

    def Set_Fan_Timer(self, time_min):
        self.device_clock.set_on_timer(time_min)
        self.Turn_On()
        
    def Process_Fan(self):
        try: 
            error = self.switch.plug_update()
            if not error:
                self.state = self.switch.get_is_on()
            timer_state = self.device_clock.process_clock()
            if timer_state == False:
                self.Turn_Off()
        except: 
            log("SIGNAL SNA", self.name)
            self.state = self.previous_state
        else:
            self.previous_state = self.state
        finally:
            pass
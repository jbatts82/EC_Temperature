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
        self.over_ride = False
        self.over_ride_state = False
        self.previous_state = False
        self.device_clock = Device_Clock()
        fan_config = next(item for item in config.plug_config if item["name"] == "exhaust")
        self.switch = KasaPlug(fan_config)
        self.Process_Fan()
        
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

    def Set_Fan_Override(self, over_ride, state):
        self.over_ride = over_ride
        self.over_ride_state = state
        
    def Process_Fan(self):
        log("Processing", self.name)
        try: 
            timer_state = self.device_clock.process_clock()
            if timer_state == False:
                self.Turn_Off()
            self.state = self.switch.error_state
        except: 
            log("SIGNAL SNA", self.name)
            self.state = self.previous_state
        else:
            self.previous_state = self.state
        finally:
            pass
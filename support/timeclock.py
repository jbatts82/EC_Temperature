###############################################################################
# File Name  : timeclock.py
# Date       : 04/09/2021
# Description: 
###############################################################################

import datetime
from datetime import timedelta
from support import log, div

class OS_Clock:
    system_start_time = datetime.datetime.now()

    def __init__(self):
        print("Processing         : Clock Initializing")

    def get_time_since_start(self):
        delta_time = datetime.datetime.now() - OS_Clock.system_start_time
        return delta_time
  
    def get_current_time_stamp(self):
        now = datetime.datetime.now()
        return now
  
    def date_now(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        today = str(today)
        return(today)

    def time_now(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        now = str(now)
        return(now)

class Device_Clock:
    def __init__(self):
        log("Processing", "Clock Initializing")
        self.clock_start_time = datetime.datetime.now()
        self.turn_off_t_stamp = self.clock_start_time
        self.timer_state = False

    def process_clock(self):
        time_now = datetime.datetime.now()
        off_time = self.turn_off_t_stamp
        
        if time_now >= off_time:
            self.timer_state = False

        return self.timer_state

    def set_on_timer(self, length_min):
        time_now = datetime.datetime.now()
        self.turn_off_t_stamp = time_now + timedelta(minutes = length_min)
        self.timer_state = True
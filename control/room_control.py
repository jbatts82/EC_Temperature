###############################################################################
# Filename    : room_control.py
# Date        : 04/10/2021 
# Description : Processes room environment data
###############################################################################

from control.humidifier import Humidifier
from control.heater import Heater
from datetime import datetime
from support import log
from support import div

def init_room_controller(the_config):

	log("Room Control", "Init")
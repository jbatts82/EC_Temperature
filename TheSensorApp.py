###############################################################################
# File Name  : TheSensorApp.py
# Date       : 03/13/2021
# Description: 
###############################################################################

from config import Config
from temp_sensing.DHT11 import DHT11
from control.leds import leds
from control.plug import KasaPlug
from support import log
import asyncio
from time import sleep


def test_plug_data(test_plug):
    log("LED Status", str(test_plug.get_led_status()))
    log("LED Alias", str(test_plug.get_plug_alias()))
    log("LED Is On", str(test_plug.get_is_on()))
    log("LED State Info", str(test_plug.get_state_info()))


def test_plug_on_off(test_plug):
    pass


def test_plug_led_on_off(test_plug):
    pass



if __name__ == '__main__':
	log("Starting", __file__)
	
	the_config = Config()
	
	sensor1 = DHT11(the_config)
	the_leds = leds(the_config)

	plug1 = KasaPlug(the_config)
	plug2 = KasaPlug(the_config)
	plug3 = KasaPlug(the_config)
	plug4 = KasaPlug(the_config)
	plug_list = [plug1, plug2, plug3, plug4]

	while True:
		for plug in plug_list:
			plug.process_plug()
			test_plug_data(plug)
		sleep(10)
	





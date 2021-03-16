###############################################################################
# File Name  : leds.py
# Date       : 03/14/2021
# Description: LED Control              
###############################################################################

from gpiozero import LED
from time import sleep
from support import log

class leds:
	def __init__(self, config):
		night_mode = True
		if config:
			led_configs = config.led_config
			led_array = []

			for led in led_configs:
				led = LED(led["pin"])
				led.on()
				sleep(1)

			log("Status", "Success")
		else:
			log("Status", "No Config Availale")
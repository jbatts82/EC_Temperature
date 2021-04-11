###############################################################################
# File Name  : leds.py
# Date       : 03/14/2021
# Description: LED Control              
###############################################################################

from gpiozero import LED
from time import sleep
from support import log

led_array = []

class Leds:
	def __init__(self, config):
		log("Initializing", "LED Array")
		night_mode = True
		if config:
			led_configs = config.led_config
			for config in led_configs:
				led = LED(config["pin"])
				led.on()
				led_array.append(led)
				led.off()
			log("Status", "Success")
		else:
			log("Status", "No Config Availale")
		log("Completed", "LED Array")

	def toggle(self, index):
		led_array[index].toggle()

	def turn_on(self, index):
		led_array[index].on()

	def turn_off(self, index):
		led_array[index].off()

	

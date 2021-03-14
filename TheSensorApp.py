###############################################################################
# File Name  : TheSensorApp.py
# Date       : 03/13/2021
# Description: 
###############################################################################

from config import Config
from temp_sensing.DHT11 import DHT11



if __name__ == '__main__':
	print("Starting           :", __file__)

	the_config = Config()
	sensor1 = DHT11(the_config)
	





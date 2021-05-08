###############################################################################
# File Name  : TheWebApp.py
# Date       : 08/24/2020
# Description: configuration 
###############################################################################

from WebApp import app

if __name__ == '__main__':
	print("Starting           :", __file__)
	app.run(host='0.0.0.0')
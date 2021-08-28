###############################################################################
# File Name  : TheWebApp.py
# Date       : 08/24/2020
# Description: configuration 
###############################################################################

from WebApp import app
from support import log
from support import div
import data.db_app as db
from config import Config
import WebApp.models as wc


if __name__ == '__main__':
	the_config = Config()
	db.Db_App_Init(the_config)
	wc.Init_Models()
	app.debug = True
	app.run(host='0.0.0.0')
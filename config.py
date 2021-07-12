###############################################################################
# File Name  : config.py
# Date       : 03/13/2021
# Description: configuration 
###############################################################################

from support import log

class Config:
    log("Initalizing", "Config")

    SECRET_KEY = 'you-will-never-guess'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYT = 23

    ROLLING_AVG_SIZE = 4
    DEQUE_SIZE = 4

    # temperature sensor configuration
    dht11_config = [{"name":"ch1", "pin":4, "sensor_type":22, "assigned": False},
                    {"name":"ch2", "pin":17, "sensor_type":22, "assigned": False},
                    {"name":"ch3", "pin":27, "sensor_type":22, "assigned": False},
                    {"name":"ch4", "pin":22, "sensor_type":22, "assigned": False}]

    sensor_retrys = 5
            
    # pin number uses gpiozero numbering
    led_config =   [{"name":"led1", "pin":21, "sensor_type":1},
                    {"name":"led2", "pin":20, "sensor_type":1},
                    {"name":"led3", "pin":16, "sensor_type":1},
                    {"name":"led4", "pin":12, "sensor_type":1},
                    {"name":"led5", "pin":7,  "sensor_type":1},
                    {"name":"led6", "pin":8,  "sensor_type":1},
                    {"name":"led7", "pin":25, "sensor_type":1},
                    {"name":"led8", "pin":24, "sensor_type":1}]

    plug_config =  [{"name": "heater", "ip": "10.0.0.171", "assigned": False},
                    {"name": "humidifier", "ip": "10.0.0.172", "assigned": False},
                    {"name": "exhaust", "ip": "10.0.0.170", "assigned": False},
                    {"name": "lamp", "ip": "10.0.0.169", "assigned": False},
                    {"name": "breeze", "ip": "10.0.0.173", "assigned": False}]

    database_loc = '/home/mario/ec2/EnvironmentController_2.0/ec_11_7_21.db'


    time_table = []
    time_table.append({"hour":0, "name":'Late Night', "temp":68})
    time_table.append({"hour":4, "name":'Early Morning', "temp":72})
    time_table.append({"hour":8, "name":'Morning', "temp":74})
    time_table.append({"hour":12, "name":'After Noon', "temp":76})
    time_table.append({"hour":16, "name":'Evening', "temp":73})
    time_table.append({"hour":20, "name":'Night', "temp":70})

    
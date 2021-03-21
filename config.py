###############################################################################
# File Name  : config.py
# Date       : 03/13/2021
# Description: configuration 
###############################################################################

from support import log

class Config:
    log("Initalizing", "Config")

    dht11_config = [{"name":"ch1", "pin":4, "sensor_type":11, "assigned": False},
                    {"name":"ch2", "pin":17, "sensor_type":11, "assigned": False},
                    {"name":"ch3", "pin":27, "sensor_type":11, "assigned": False},
                    {"name":"ch4", "pin":22, "sensor_type":11, "assigned": False}]
            
    # pin number uses gpiozero numbering
    led_config =   [{"name":"led1", "pin":21, "sensor_type":1},
                    {"name":"led2", "pin":20, "sensor_type":1},
                    {"name":"led3", "pin":16, "sensor_type":1},
                    {"name":"led4", "pin":12, "sensor_type":1},
                    {"name":"led5", "pin":7,  "sensor_type":1},
                    {"name":"led6", "pin":8,  "sensor_type":1},
                    {"name":"led7", "pin":25, "sensor_type":1},
                    {"name":"led8", "pin":24, "sensor_type":1}]

    plug_config =  [{"name": "plug1", "ip": "10.0.0.170", "assigned": False},
                    {"name": "plug2", "ip": "10.0.0.171", "assigned": False},
                    {"name": "plug3", "ip": "10.0.0.172", "assigned": False},
                    {"name": "plug4", "ip": "10.0.0.173", "assigned": False}]

    database_loc = '/home/mario/ec2/EnvironmentController_2.0/ec2.db'

    log("Completed", "Config")
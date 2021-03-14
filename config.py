###############################################################################
# File Name  : config.py
# Date       : 03/13/2021
# Description: configuration 
###############################################################################


class Config:
    # Sensor Configurations
    sensor_cnt = 4
    sensor_configs = []
    sensor_configs.append({"name":"ch1", "data_pin":4, "sensor_type":11})
    sensor_configs.append({"name":"ch2", "data_pin":17, "sensor_type":11})
    sensor_configs.append({"name":"ch3", "data_pin":27, "sensor_type":11})
    sensor_configs.append({"name":"ch4", "data_pin":22, "sensor_type":11})
    

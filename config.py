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
    
    # LED Configuration
    # LED1->Phy40->gpiozero_21
	# LED2->Phy38->gpiozero_20
	# LED3->Phy36->gpiozero_16
	# LED4->Phy32->gpiozero_12
	# LED5->Phy26->gpiozero_7
	# LED6->Phy24->gpiozero_8
	# LED7->Phy22->gpiozero_25
	# LED8->Phy18->gpiozero_24
    led_cnt = 8
    led_configs = []
    led_configs.append({"name":"led1", "pin":21, "sensor_type":1})
    led_configs.append({"name":"led2", "pin":20, "sensor_type":1})
    led_configs.append({"name":"led3", "pin":16, "sensor_type":1})
    led_configs.append({"name":"led4", "pin":12, "sensor_type":1})
    led_configs.append({"name":"led5", "pin":7,  "sensor_type":1})
    led_configs.append({"name":"led6", "pin":8,  "sensor_type":1})
    led_configs.append({"name":"led7", "pin":25, "sensor_type":1})
    led_configs.append({"name":"led8", "pin":24, "sensor_type":1})


    kasa_devices = [{"name": "pam", "ip": "10.0.0.170", "assigned": False},
                    {"name": "pat", "ip": "10.0.0.171", "assigned": False},
                    {"name": "paul", "ip": "10.0.0.172", "assigned": False}]
###############################################################################
# File Name  : plug.py
# Date       : 03/14/2021
# Description: Controls TPLink Smart Plugs           
###############################################################################

import asyncio
from kasa import SmartPlug
from time import sleep
from support import log
from datetime import datetime

def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            # input function
            func(*args, **kwargs)
            error_state = False
        except Exception as e:
            error_state = True
            log("Error", "Exception Found!!!")
            log("Error Message", "{}".format(e))
            error_state = True
        return error_state
    return inner_function

class KasaPlug:
    def __init__(self, device_list):
        log("Initializing", "Kasa Plug")
        self.error_state = True
        
        if device_list.plug_config:  # is available
            # find unused device
            for device in device_list.plug_config:
                if not device["assigned"]:
                    device["assigned"] = True
                    self.name = device["name"]
                    self.ip = device["ip"]
                    break
            else:
                log("Error", "All Kasa Plugs In Use")
                return
        else:
            log("Error", "No Config Available")
            return

        self.smart_plug = SmartPlug(self.ip)
        self.process_plug()
        self.set_led_off()

    def process_plug(self):
        self.error_state = self.plug_update()
        log("Process Plug Error", str(self.error_state))

    # Only call through process plug to log any errors
    @exception_handler
    def plug_update(self):
        now = datetime.now()
        log("Plug Update Start", str(now))
        asyncio.run(self.smart_plug.update())
        after = datetime.now()
        log("Plug Update Finish", str(after))
        log("Difference", str(after - now))

    @exception_handler
    def set_led_on(self):
        result = asyncio.run(self.smart_plug.set_led(True))
        log("Result", result)

    @exception_handler
    def set_led_off(self):
        asyncio.run(self.smart_plug.set_led(False))

    @exception_handler
    def set_plug_on(self):
        asyncio.run(self.smart_plug.turn_on())

    @exception_handler
    def set_plug_off(self):
        asyncio.run(self.smart_plug.turn_on())

    def get_led_status(self):
        return self.smart_plug.led

    def get_plug_alias(self):
        return self.smart_plug.alias

    def get_is_on(self):
        return self.smart_plug.is_on

    def get_state_info(self):
        return self.smart_plug.state_information


# end KasaPlug ###############################################################


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
    print("Starting File: ", __file__)
    plug1 = KasaPlug(kasa_devices)
    plug2 = KasaPlug(kasa_devices)
    plug3 = KasaPlug(kasa_devices)
    plug4 = KasaPlug(kasa_devices)
    plug_list = [plug1, plug2, plug3, plug4]

    while True:
        for plug in plug_list:
            plug.process_plug()
            test_plug_data(plug)
        sleep(5)
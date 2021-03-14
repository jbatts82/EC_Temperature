# EC_Temperature



Hardware Platform: Raspberry Pi B+

Rpi Provisioning Steps:
- Set up Linux OS
- Raspi-Config
	- enable i2c, spi, gpio
- Set up Samba.
- Set up pip3
- set up wiringPi
- python3-gpiozero
- Set up virtualenv with pip
- anything else?


- Temperature HW  Config


# Libraries Needed
python3 -m pip freeze > requirements.txt
python3 -m pip install -r requirements.txt
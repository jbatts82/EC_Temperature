# EC_Temperature

Hardware Platform: Raspberry Pi B+

Rpi Provisioning Steps:
- Set up Linux OS
- raspi-Config
	- enable i2c, spi, gpio
- samba.
- pip3
	- wiringPi
	- sqlite3
	- python3-gpiozero
	- python-kasa
	- virtualenv
- sqlite3
- Temperature HW  Config


# Python requirements
python3 -m pip freeze > requirements.txt
python3 -m pip install -r requirements.txt
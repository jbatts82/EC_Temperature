###############################################################################
# File Name  : forms.py
# Date       : 08/24/2020
# Description: Fields are defined as class variables. 
###############################################################################

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired
from config import Config

class GraphConfigForm(FlaskForm):
	time = IntegerField('Minutes To Graph')
	submit = SubmitField('Submit')

class Data_To_Show(FlaskForm):
	show_heater = BooleanField("Heater")
	show_light = BooleanField("Light")
	show_fan = BooleanField("Fan")
	show_ch1 = BooleanField("Channel 1")
	show_ch2 = BooleanField("Channel 2")
	show_ch3 = BooleanField("Channel 3")
	show_ch4 = BooleanField("Channel 4")
	time = IntegerField('Minutes To Graph')

class FanOverride(FlaskForm):
	is_fan_override = BooleanField("Fan Override")
	fan_override_state = BooleanField("Fan State")

class HeaterOverride(FlaskForm):
	is_heater_override = BooleanField("Heater Override")
	heater_override_state = BooleanField("Heater State")
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
	sensor_name = SelectField(u'Sensor Name', choices=[('plant1', 'Sensor 1'), ('plant2', 'Sensor 2'), ('intake_air', 'Sensor 3'), ('upper_room_air', 'Sensor 4')])
	time = IntegerField('Begin Graph X Mins Ago')
	submit = SubmitField('Submit')
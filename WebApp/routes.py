###############################################################################
# File Name  : routes.py
# Date       : 07/11/2020
# Description: Displays sensor output to web page.
###############################################################################

from flask import render_template, flash, redirect, url_for, Flask, send_file, make_response, request, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import io
import random
from WebApp import forms
from WebApp import app
from config import Config
import data.db_app as db

from support import log
from support import div


@app.route('/')
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():

    global time_arr, temp_arr, hum_arr, heat_state_arr, hum_state_arr, fan_state_arr, light_state_arr, control_time_arr
    time_arr = []
    temp_arr = []
    hum_arr = []

    heat_state_arr = []
    hum_state_arr = []
    fan_state_arr = []
    light_state_arr = []
    control_time_arr = []

    config = Config()
    _title = 'Plant Life'
    channel = 'ch1'
    previous_minutes_back = 200



    # User Input
    data_to_show = forms.Data_To_Show()
    graphConfig = forms.GraphConfigForm()
    if graphConfig.validate_on_submit():
        minutes = graphConfig.time.data
        channel = graphConfig.channel.data
        previous_minutes_back = minutes
        is_hum = data_to_show.show_hum.data
    

    # Sensor Data
    sensor_recs = db.Get_Last_Sensor_List(channel, previous_minutes_back)
    for record in sensor_recs:
        time_arr.append(record.time_stamp)
        temp_arr.append(record.temperature)
        hum_arr.append(record.humidity)

    # Control Data
    control_recs = db.Get_Last_Control_List(previous_minutes_back)
    for rec in control_recs:
        heat_state_arr.append(rec.heater_state)
        hum_state_arr.append(rec.humidifier_state)
        fan_state_arr.append(rec.fan_state)
        light_state_arr.append(rec.light_state)
        control_time_arr.append(rec.time_stamp)

    # Sensor Data
    sensor_data = {}
    for each in config.dht11_config:
        channel = each['name']
        record = db.Get_Last_Sensor_Rec(channel)
        sensor_data[channel] = {"temp":record.temperature, "humidity":record.humidity, "time_temp":record.time_stamp}

    return render_template('index.html', title=_title, data = sensor_data, graph_form=graphConfig, control_form=data_to_show)

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    global time_arr, temp_arr, hum_arr
    fig = Figure(figsize=(10,20))
    xs = time_arr
    ys = temp_arr
    axis = fig.add_subplot(6, 1, 1, xlabel='Time', ylabel='Temperature')
    axis.plot(xs, ys)

    ys = hum_arr
    axis = fig.add_subplot(6, 1, 2, xlabel='Time', ylabel='Humidity')
    axis.plot(xs, ys)

    xs = control_time_arr
    ys = heat_state_arr
    axis = fig.add_subplot(6, 1, 3, xlabel='Control Time', ylabel='Heater State', yticks=(0,1))
    axis.plot(xs, ys)

    ys = hum_state_arr
    axis = fig.add_subplot(6, 1, 4, xlabel='Control Time', ylabel='Humidifier State', yticks=(0,1))
    axis.plot(xs, ys)

    ys = fan_state_arr
    axis = fig.add_subplot(6, 1, 5, xlabel='Control Time', ylabel='Fan State', yticks=(0,1))
    axis.plot(xs, ys)
    
    ys = light_state_arr
    axis = fig.add_subplot(6, 1, 6, xlabel='Control Time', ylabel='Light State', yticks=(0,1))
    axis.plot(xs, ys)

    return fig
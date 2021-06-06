###############################################################################
# File Name  : routes.py
# Date       : 07/11/2020
# Description: Displays sensor output to web page.
###############################################################################

from flask import render_template, flash, redirect, url_for, Flask, send_file, make_response, request, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import io
import base64
import random
from WebApp import forms
from WebApp import app
from config import Config
import data.db_app as db

from support import log
from support import div
import json


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
    previous_minutes_back = 240

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

    # User Input
    data_to_show = forms.Data_To_Show()
    show_temperature = data_to_show.show_temperature.data
    show_heater = data_to_show.show_heater.data

    graphConfig = forms.GraphConfigForm()
    if graphConfig.validate_on_submit():
        minutes = graphConfig.time.data
        channel = graphConfig.channel.data
        previous_minutes_back = minutes


    g64 = {}
    figure = create_figure(10, 5)
    axes = add_axes(figure, "The Graph", "Time", "Temperature" )
    add_line(axes, time_arr, temp_arr, "temp")
    g64["temp"] = plot_png(figure)

    return render_template('index.html', title=_title, data = sensor_data, graph_form=graphConfig, data_to_show=data_to_show, graph1b64=g64)

@app.route('/toggle_humidity_graph', methods=['GET', 'POST'])
def toggle_humidity_graph():
    json_data = request.form['graph_data']
    the_data = json.loads(json_data) 
    show_graph = the_data["show_humidity"]

    if show_graph:
        log("Graph", "on")
    else:
        log("Graph", "off")

    ret_val = { 'error' : False }
    
    return json.dumps(ret_val)


def create_figure(x_size, y_size):
    global hum_arr
    figure = Figure(figsize=(x_size, y_size))
    return figure

def add_axes(figure, title, x_label, y_label):
    axis = figure.add_subplot(1, 1, 1, xlabel=x_label, ylabel=y_label)
    return axis

def add_line(axis, xs, ys, id):
    lines = axis.plot(xs, ys, gid=id)
    return lines

def remove_line(axis, id):
    for line in axis.lines():
        if line.get_gid() == id:
            line.remove()

def plot_png(fig):
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    stbytes = output.getvalue()
    data = base64.b64encode(stbytes).decode("ascii")
    return data
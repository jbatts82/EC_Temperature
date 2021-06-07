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
from WebApp.mat_graph import MatGraph

@app.route('/')
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():

    global time_arr, temp_arr, hum_arr, heat_state_arr, hum_state_arr, fan_state_arr, light_state_arr, control_time_arr, the_graph
    time_arr = []
    temp_arr = []
    hum_arr = []
    heat_state_arr = []
    hum_state_arr = []
    fan_state_arr = []
    light_state_arr = []
    control_time_arr = []

    config = Config()


    the_graph = MatGraph(config)
    the_graph.add_axes("A Tit", "Time", "Garden Gaden")

    _title = 'Plant Life'
    channel = 'ch1'
    previous_minutes_back = 600

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


    return render_template('index.html', title=_title, data = sensor_data, graph_form=graphConfig, data_to_show=data_to_show, graph1b64 = None)


@app.route('/toggle_humidity_graph', methods=['GET', 'POST'])
def toggle_humidity_graph():
    global the_graph, time_arr, hum_arr
    json_data = request.form['graph_data']
    the_data = json.loads(json_data) 
    show_graph = the_data["show_humidity"]

    if show_graph:
        log("Graph", "on")
        the_graph.add_line(time_arr, hum_arr, "hum")
        png64data = the_graph.plot_png()
        data_string = "data:image/png;base64,{}".format(png64data)

    else:
        log("Graph", "off")
        data_string = ""

    ret_val = { 'error' : False, 'the_graph' :  data_string}
    return json.dumps(ret_val)

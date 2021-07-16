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


config = Config()


@app.route('/')
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():

    global data_arr, config

    data_arr = {
        "time_arr":[],
        "time2_arr":[],
        "temp_arr":[],
        "hum_arr":[],
        "heat_state_arr":[],
        "hum_state_arr":[],
        "fan_state_arr":[],
        "light_state_arr":[],
        "control_time_arr":[]
    }

    _title = 'Plant Life'
    channel = 'ch1'
    previous_minutes_back = 120

    graphConfig = forms.GraphConfigForm()
    if graphConfig.validate_on_submit():
        minutes = graphConfig.time.data
        channel = graphConfig.channel.data
        previous_minutes_back = minutes


    # Sensor Data
    sensor_recs = db.Get_Last_Sensor_List(channel, previous_minutes_back)
    for record in sensor_recs:
        data_arr["time_arr"].append(record.time_stamp)
        data_arr["temp_arr"].append(record.temperature)
        data_arr["hum_arr"].append(record.humidity)

    # Control Data
    control_recs = db.Get_Last_Control_List(previous_minutes_back)
    for rec in control_recs:
        data_arr["heat_state_arr"].append(rec.heater_state)
        data_arr["hum_state_arr"].append(rec.humidifier_state)
        data_arr["fan_state_arr"].append(rec.fan_state)
        data_arr["light_state_arr"].append(rec.light_state)
        data_arr["time2_arr"].append(rec.time_stamp)

    # Sensor Data
    sensor_data = {}
    for each in config.dht11_config:
        channel = each['name']
        record = db.Get_Last_Sensor_Rec(channel)
        sensor_data[channel] = {"temp":record.temperature, "humidity":record.humidity, "time_temp":record.time_stamp}

    # User Input
    data_to_show = forms.Data_To_Show()


    return render_template('index.html', title=_title, data = sensor_data, graph_form=graphConfig, data_to_show=data_to_show, graph1b64 = None)


@app.route('/set_graph_lines', methods=['GET', 'POST'])
def set_graph_lines():
    global the_graph
    json_data = request.form['graph_data']
    the_data = json.loads(json_data)
    the_graph = MatGraph(config)
    update_temperature_graph(the_data)
    update_humidity_graph(the_data)
    png64data = the_graph.plot_png()
    data_string = "data:image/png;base64,{}".format(png64data)
    ret_val = { 'error' : False, 'the_graph' :  data_string}
    return json.dumps(ret_val)


# entry point
def update_temperature_graph(req_graph_lines):
    global data_arr, the_graph
    the_graph.add_line_temp(data_arr["time_arr"], data_arr["temp_arr"], "temp", "black")


def update_humidity_graph(req_graph_lines):
    global data_arr, the_graph
    the_graph.add_line_humid(data_arr["time_arr"], data_arr["hum_arr"], "hum", "black")
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
from support import log, div
import json
from WebApp.mat_graph import MatGraph
import WebApp.models as wc
from support.timeclock import OS_Clock

config = Config()

@app.route('/')
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():

    log("index", "Here")
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
    previous_minutes_back = 1440

    graphConfig = forms.GraphConfigForm()
    if graphConfig.validate_on_submit():
        log("GraphConfig", "Sumbit")
        previous_minutes_back = graphConfig.time.data


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
    fan_override = forms.FanOverride()
    heater_override = forms.HeaterOverride()

    return render_template('index.html', 
                            title=_title, 
                            data = sensor_data, 
                            graph_form=graphConfig, 
                            data_to_show=data_to_show, 
                            graph1b64 = None,
                            fan_override=fan_override,
                            heater_override = heater_override)


@app.route('/set_web_req', methods=['GET', 'POST'])
def set_web_req():
    json_data = request.form['data']
    the_data = json.loads(json_data)
    # set web control table
    wc.Update_Web_Control_Table(the_data)
    ret_val = {'error' : False}
    return json.dumps(ret_val)


@app.route('/set_graph_data', methods=['GET', 'POST'])
def set_graph_data():
    global the_graph
    json_data = request.form['graph_data']
    the_data = json.loads(json_data)
    the_graph = MatGraph(config)
    update_graph(the_data)
    png64data = the_graph.plot_png()
    data_string = "data:image/png;base64,{}".format(png64data)
    ret_val = {'error' : False, 'the_graph' :  data_string}
    return json.dumps(ret_val)


def update_graph(req_graph_lines):
    global data_arr, the_graph
    the_graph.update_graph(req_graph_lines, data_arr)


@app.route('/update_model', methods=['GET', 'POST'])
def update_model():
    json_data = request.form['data']
    log("json_data", json_data)
    client_model = json.loads(json_data)
    wc.update_client_webcontrol(web_control)
    server_model = wc.get_web_model()
    ret_val = {'error' : False, 'data' :  server_model}
    return json.dumps(ret_val)


@app.route('/get_server_model', methods=['GET', 'POST'])
def get_server_model():
    json_data = request.form['cmd']
    log("json_data", json_data)
    server_model = wc.get_model()
    ret_val = {'error' : False, 'server_model' : server_model}
    return json.dumps(ret_val)


@app.route('/send_client_model', methods=['GET', 'POST'])
def send_client_model():
    json_data = request.form['client_model']
    log("clientModel", json_data)
    client_model = json.loads(json_data)
    wc.update_client_model(client_model)
    server_model = wc.get_model()
    ret_val = {'error' : False, 'server_model' : server_model}
    return json.dumps(ret_val)
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

@app.route('/')
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
@app.route('/index', methods=['GET', 'POST'])
def index():
    global time_arr, temp_arr
    time_arr = []
    temp_arr = []
    
    config = Config()
    _title = 'Plant Life'
    channel = 'ch1'
    previous_minutes_back = 60

    graphConfig = forms.GraphConfigForm()
    if graphConfig.validate_on_submit():
        minutes = graphConfig.time.data
        channel = graphConfig.channel.data
        previous_minutes_back = minutes

    temp_recs = db.Get_Last_Temp_List(channel, previous_minutes_back)

    for temp in temp_recs:
        time_arr.append(temp.time_stamp)
        temp_arr.append(temp.temperature)

    return render_template('index.html', title=_title, data = [1, 2, 3, 4], form=graphConfig)

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    global time_arr, temp_arr
    fig = Figure(figsize=(1,1))
    xs = time_arr
    ys = temp_arr
    axis = fig.add_subplot(6, 1, 1, xlabel='Time', ylabel='Temperature')
    axis.plot(xs, ys)

    # ys = hum_arr
    # axis = fig.add_subplot(6, 1, 2, xlabel='Time', ylabel='Humidity')
    # axis.plot(xs, ys)

    # xs = control_time
    # ys = heater_state
    # axis = fig.add_subplot(6, 1, 3, xlabel='Control Time', ylabel='Heater State', yticks=(0,1))
    # axis.plot(xs, ys)

    # ys = humidifier_state
    # axis = fig.add_subplot(6, 1, 4, xlabel='Control Time', ylabel='Humidifier State', yticks=(0,1))
    # axis.plot(xs, ys)

    # ys = fan_state
    # axis = fig.add_subplot(6, 1, 5, xlabel='Control Time', ylabel='Fan State', yticks=(0,1))
    # axis.plot(xs, ys)
    
    # ys = light_state
    # axis = fig.add_subplot(6, 1, 6, xlabel='Control Time', ylabel='Light State', yticks=(0,1))
    # axis.plot(xs, ys)

    return fig
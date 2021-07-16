###############################################################################
# File Name  : mat_graph.py
# Date       : 06/06/2021
# Description: Class to hold graph data
###############################################################################

from flask import render_template, flash, redirect, url_for, Flask, send_file, make_response, request, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from support import log
import io
import base64

x_width = 15
y_width = 7.5

graph_layout = {
	"temp": {"temp":False, "heater":False, "light":False, "fan":False},
	"hum": {"temp":False, "heater":False, "light":False, "fan":False}
}

'''
Create a Figure object. , then add an Axes, ax and figure.axes[0] are same object. 


'''



class MatGraph:
	def __init__(self, config):
		self.figure = Figure(figsize=(x_width, y_width))
		self.axe_temp = self.figure.add_subplot(2, 1, 1, title = "Room Data", xlabel="Time", ylabel="Temperature (F)")
		self.axe_humid = self.figure.add_subplot(2, 1, 2, title = "Room Data", xlabel="Time", ylabel="Humidity (%)")


	def add_line_temp(self, xs, ys, id, color):
		self.axe_temp.plot(xs, ys, gid=id, color=color)


	def add_line_humid(self, xs, ys, id, color):
		self.axe_humid.plot(xs, ys, gid=id, color=color)


	def remove_line_temp(self, id):
		for line in self.axe_temp.lines:
			if line.get_gid() == id:
				line.remove()

	def remove_line_humid(self, id):
		for line in self.axe_humid.lines:
			if line.get_gid() == id:
				line.remove()


	def plot_png(self):
		output = io.BytesIO()
		FigureCanvasAgg(self.figure).print_png(output)
		stbytes = output.getvalue()
		data = base64.b64encode(stbytes).decode("ascii")
		return data
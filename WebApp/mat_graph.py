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

x_width = 10
y_width = 5


# MatGraph should have only 1 figure, can have multiple axes
class MatGraph:
	def __init__(self, config):
		self.figure = Figure(figsize=(x_width, y_width))
		self.axis = []
		self.lines = []

	def add_axes(self, title, x_label, y_label):
	    self.axis.append(self.figure.add_subplot(1, 1, 1, title = title, xlabel=x_label, ylabel=y_label))
	    
	def add_line(self, xs, ys, id):
	    self.lines.append(self.axis[0].plot(xs, ys, gid=id))

	def remove_line(self, id):
	    for line in self.axis.lines():
	        if line.get_gid() == id:
	            line.remove()

	def plot_png(self):
		output = io.BytesIO()
		FigureCanvasAgg(self.figure).print_png(output)
		stbytes = output.getvalue()
		data = base64.b64encode(stbytes).decode("ascii")
		return data
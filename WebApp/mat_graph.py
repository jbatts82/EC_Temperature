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


'''
Create a Figure object. , then add an Axes, ax and fig.axes[0] are same object. 



'''

class MatGraph:
	def __init__(self, config):
		self.figure = Figure(figsize=(x_width, y_width))
		self.line_states = {
			"temp": False,
			"hum": False,
			"heater": False,
			"light": False,
			"fan": False,
		}

		self.ax = None

	def add_axes(self, title, x_label, y_label):
		self.ax = self.figure.add_subplot(1, 1, 1, title = title, xlabel=x_label, ylabel=y_label)


	def add_line(self, xs, ys, id, color):
		#check if already added
		log("ALready Added", self.line_states[id])
		if self.line_states[id]:
			return

		#check if this is first line or additional
		log("Is first line?", self.lines_states.values())
		for value in self.lines_states.values():
			if value:
				# additional line path
				self.ax2 = self.ax.twinx()
				self.ax2.plot(xs, ys, gid=id, color=color)
				self.ax2.set_ylabel(id,color="blue",fontsize=14)
				break; # or just return
		else:
			# first line path
			self.line_states[id] =  True
			lines = self.ax.plot(xs, ys, gid=id, color=color)


	def remove_line(self, id):
		self.line_states[id] =  False
		for line in self.ax.lines:
			if line.get_gid() == id:
				print("found")
				line.remove()

	def plot_png(self):
		output = io.BytesIO()
		FigureCanvasAgg(self.figure).print_png(output)
		stbytes = output.getvalue()
		data = base64.b64encode(stbytes).decode("ascii")
		return data
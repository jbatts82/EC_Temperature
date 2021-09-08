###############################################################################
# File Name  : mat_graph.py
# Date       : 06/06/2021
# Description: Class to hold graph data
###############################################################################

from flask import render_template, flash, redirect, url_for, Flask, send_file, make_response, request, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from support import log, div
import io
import base64

x_width = 20
y_width = 15



'''
Create a Figure object. , then add an Axes, ax and figure.axes[0] are same object. 


'''



class MatGraph:
	def __init__(self, config):
		self.figure = Figure(figsize=(x_width, y_width))
		self.plot_axes = {
			"fehr": self.figure.add_subplot(3, 1, 1, title = "Room Data", xlabel="Time", ylabel="Temperature (F)"),
			"percent": self.figure.add_subplot(3, 1, 2, title = "Room Data", xlabel="Time", ylabel="Humidity (%)"),
			"bool" : self.figure.add_subplot(3, 1, 3, title = "Room Data", xlabel="Time", ylabel="Device States (bool)"),
		}


	def update_graph(self, req_graph_lines, data_arr):
		log("Time Length", len(data_arr["time_arr"]))
		log("ch1 temp arr", len(data_arr["sensor_data"]["ch1"]["temp_arr"]))
		log("ch2 temp arr", len(data_arr["sensor_data"]["ch2"]["temp_arr"]))
		log("ch3 temp arr", len(data_arr["sensor_data"]["ch3"]["temp_arr"]))
		log("ch4 temp arr", len(data_arr["sensor_data"]["ch4"]["temp_arr"]))
		log("ch1 hum arr", len(data_arr["sensor_data"]["ch1"]["hum_arr"]))
		log("ch2 hum arr", len(data_arr["sensor_data"]["ch2"]["hum_arr"]))
		log("ch3 hum arr", len(data_arr["sensor_data"]["ch3"]["hum_arr"]))
		log("ch4 hum arr", len(data_arr["sensor_data"]["ch4"]["hum_arr"]))

		if req_graph_lines["ch1"]:
			self.equalize_lists(data_arr["time_arr"], data_arr["sensor_data"]["ch1"]["temp_arr"])
			self.add_line_fehr(data_arr["time_arr"], data_arr["sensor_data"]["ch1"]["temp_arr"], "temp", "red")
			self.add_line_percent(data_arr["time_arr"], data_arr["sensor_data"]["ch1"]["hum_arr"], "hum", "red")
		else:
			self.remove_line_fehr("ch1")
			self.remove_line_percent("ch1")

		if req_graph_lines["ch2"]:
			self.equalize_lists(data_arr["time_arr"], data_arr["sensor_data"]["ch2"]["temp_arr"])
			self.add_line_fehr(data_arr["time_arr"], data_arr["sensor_data"]["ch2"]["temp_arr"], "temp", "orange")
			self.add_line_percent(data_arr["time_arr"], data_arr["sensor_data"]["ch2"]["hum_arr"], "hum", "orange")
		else:
			self.remove_line_fehr("ch2")
			self.remove_line_percent("ch2")

		if req_graph_lines["ch3"]:
			self.equalize_lists(data_arr["time_arr"], data_arr["sensor_data"]["ch3"]["temp_arr"])
			self.add_line_fehr(data_arr["time_arr"], data_arr["sensor_data"]["ch3"]["temp_arr"], "temp", "yellow")
			self.add_line_percent(data_arr["time_arr"], data_arr["sensor_data"]["ch3"]["hum_arr"], "hum", "yellow")
		else:
			self.remove_line_fehr("ch3")
			self.remove_line_percent("ch3")

		if req_graph_lines["ch4"]:
			self.equalize_lists(data_arr["time_arr"], data_arr["sensor_data"]["ch4"]["temp_arr"])
			self.add_line_fehr(data_arr["time_arr"], data_arr["sensor_data"]["ch4"]["temp_arr"], "temp", "green")
			self.add_line_percent(data_arr["time_arr"], data_arr["sensor_data"]["ch4"]["hum_arr"], "hum", "green")
		else:
			self.remove_line_fehr("ch4")
			self.remove_line_percent("ch4")

		div()
		log("Time Length", len(data_arr["time_arr"]))
		log("ch1 temp arr", len(data_arr["sensor_data"]["ch1"]["temp_arr"]))
		log("ch2 temp arr", len(data_arr["sensor_data"]["ch2"]["temp_arr"]))
		log("ch3 temp arr", len(data_arr["sensor_data"]["ch3"]["temp_arr"]))
		log("ch4 temp arr", len(data_arr["sensor_data"]["ch4"]["temp_arr"]))
		log("ch1 hum arr", len(data_arr["sensor_data"]["ch1"]["hum_arr"]))
		log("ch2 hum arr", len(data_arr["sensor_data"]["ch2"]["hum_arr"]))
		log("ch3 hum arr", len(data_arr["sensor_data"]["ch3"]["hum_arr"]))
		log("ch4 hum arr", len(data_arr["sensor_data"]["ch4"]["hum_arr"]))

		if req_graph_lines["heater"]:
			self.add_line_bool(data_arr["time2_arr"], data_arr["heat_state_arr"], "heater", "red")
		else:
			self.remove_line_bool("temp")

		if req_graph_lines["light"]:
			self.add_line_bool(data_arr["time2_arr"], data_arr["light_state_arr"], "light", "blue")
		else:
			self.remove_line_bool("light")

		if req_graph_lines["fan"]:
			self.add_line_bool(data_arr["time2_arr"], data_arr["fan_state_arr"], "fan", "green")
		else:
			self.remove_line_bool("fan")


	def add_line_fehr(self, xs, ys, id, color):
		self.plot_axes["fehr"].plot(xs, ys, gid=id, color=color)


	def add_line_percent(self, xs, ys, id, color):
		self.plot_axes["percent"].plot(xs, ys, gid=id, color=color)


	def add_line_bool(self, xs, ys, id, color):
		self.plot_axes["bool"].plot(xs, ys, gid=id, color=color)


	def remove_line_bool(self, id):
		for line in self.plot_axes["bool"].lines: 
			if line.get_gid() == id:
				line.remove()


	def remove_line_fehr(self, id):
		for line in self.plot_axes["fehr"].lines:
			if line.get_gid() == id:
				line.remove()


	def remove_line_percent(self, id):
		for line in self.plot_axes["percent"].lines: 
			if line.get_gid() == id:
				line.remove()

	def equalize_lists(self, time_list, list_2):
		time_len = len(time_list)
		list_len = len(list_2)

		if time_len == list_len:
			return 0

		if time_len > list_len:
			delta = time_len - list_len

			for index in range(0, delta):
				time_list.pop()






	def plot_png(self):
		output = io.BytesIO()
		FigureCanvasAgg(self.figure).print_png(output)
		stbytes = output.getvalue()
		data = base64.b64encode(stbytes).decode("ascii")
		return data
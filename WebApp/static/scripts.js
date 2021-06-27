// helper_script.js



var graph_lines = { //to show
	"temp": false,
	"hum": false,
	"heater": false,
	"light": false,
	"fan": false
};


// after page loads
$(document).ready(function() {
	update_graph_lines();
	set_graph_lines();
});

function update_graph_lines() {

	if ($('#show_temperature').is(":checked")) {
		graph_lines.temp = true;
	}
	else {
		graph_lines.temp = false;
	}

	if ($('#show_humidity').is(":checked")) {
		graph_lines.hum = true;
	}
	else {
		graph_lines.hum = false;
	}

	if ($('#show_heater').is(":checked")) {
		graph_lines.heater = true;
	}
	else {
		graph_lines.heater= false;
	}

	if ($('#show_light').is(":checked")) {
		graph_lines.light= true;
	}
	else {
		graph_lines.light = false;
	}

	if ($('#show_fan').is(":checked")) {
		graph_lines.fan = true;
	}
	else {
		graph_lines.fan = false;
	}
}

function set_graph_lines() {
	$.post( "/set_graph_lines", {
	  graph_data: JSON.stringify(graph_lines)
	}, function(resp){

		var the_64data = JSON.parse(resp);

		if (the_64data.error == true)
		{
			alert("Error");
		}
		else
		{
			$("#graph1").attr("src", the_64data.the_graph);
		}
	});
}

function update_graph() {
	update_graph_lines();
	set_graph_lines();
}
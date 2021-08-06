// helper_script.js



var graph_lines = { //to show
	"temp": false,
	"hum": false,
	"heater": false,
	"light": false,
	"fan": false
};

var fan_override = {
	"is_override": false, 
	"fan_state": false
}


// after page loads
$(document).ready(function() {
	update_graph()
});

function update_fan_override_state() {

	if ($('#is_fan_override').is(":checked")) {
		fan_override.is_override = true;
	}
	else {
		fan_override.is_override= false;
	}

	if ($('#fan_override_state').is(":checked")) {
		fan_override.fan_state = true;
	}
	else {
		fan_override.fan_state= false;
	}
}

function update_graph_lines() {

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

		}
		else
		{
			$("#graph1").attr("src", the_64data.the_graph);
		}
	});
}

function send_data(loc, data_to_send) {
	$.post( loc, {
	  data: JSON.stringify(data_to_send)
	}, function(resp){

		var the_resp = JSON.parse(resp);

		if (the_resp.error == true)
		{
			alert("Error");
		}
		else
		{
			alert("no Error")
		}
	});

}


function update_fan_override() {
	update_fan_override_state();
	send_data();
}

function update_graph() {
	update_graph_lines();
	set_graph_lines("/set_fan_override", );
}
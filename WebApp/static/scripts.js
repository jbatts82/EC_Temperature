// helper_script.js



var graph_lines = { //to show
	"temp": false,
	"hum": false,
	"heater": false,
	"light": false,
	"fan": false
};


var web_control = {
    "heater_req": false,
    "heater_state": false,
    "humidifier_req": false,
    "humidifier_state": false,
    "fan_req": false,
    "fan_state": false,
    "light_req": false,
    "light_state": false,
}


// after page loads
$(document).ready(function() {
	update_graph()
});


// html functions
function update_web_control() {
	update_fan_override_state();
	send_data('/set_web_req', web_control);
}


// Data functions
function update_fan_override_state() {

	if ($('#is_fan_override').is(":checked")) {
		web_control.fan_req = true;
	}
	else {
		web_control.fan_req= false;
	}

	if ($('#fan_override_state').is(":checked")) {
		web_control.fan_state = true;
	}
	else {
		web_control.fan_state= false;
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

		}
	});

}


function update_graph() {
	update_graph_lines();
	set_graph_lines("/set_fan_override", );
}
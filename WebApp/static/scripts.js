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
	// get data to show

	if ($('#show_temperature').is(":checked")) {
		graph_lines["temp"] = true;
	}

	if ($('#show_humidity').is(":checked")) {
		graph_lines["hum"] = true;
	}

	if ($('#show_heater').is(":checked")) {
		graph_lines["heater"] = true;
	}

	if ($('#show_light').is(":checked")) {
		graph_lines["light"] = true;
	}

	if ($('#show_fan').is(":checked")) {
		graph_lines["fan"] = true;
	}

	post_up()

	// build graph and
});


function toggle_hum() {
	var is_checked = $('#show_humidity').is(":checked")

	var the_data = {"show_humidity":is_checked}

	$.post( "/toggle_humidity_graph", {
	  graph_data: JSON.stringify(the_data)
	}, function(resp){

		the_64data = JSON.parse(resp)

		if (the_64data.error == true)
		{
			alert("Error")
		}
		else
		{
			$("#graph1").attr("src", the_64data.the_graph);
		}
	});

}
-
function post_up(path, req_data) {
	$.post(path, 
	{graph_data: json_data},
	function(data, status, xhr) {
		response = JSON.parse(data)
	});

	return response.the_graph
}

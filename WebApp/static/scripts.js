// helper_script.js

$(document).ready(function() {
	$("#demo").html("Hello, World!");
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


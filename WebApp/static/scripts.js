// helper_script.js

$(document).ready(function() {
	$("#demo").html("Hello, World!");
});


function toggle_hum() {
	var is_checked = $('#show_humidity').is(":checked")

	var the_data = {"show_humidity":is_checked}

	$.post( "/toggle_humidity_graph", {
	  graph_data: JSON.stringify(the_data)
	}, function(err, req, resp){
	 window.location.href = "/results/"+resp["responseJSON"]["error"];  
	});

}


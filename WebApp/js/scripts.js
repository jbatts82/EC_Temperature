// scripts.js

$(document).ready(function() {
	$("#demo").html("Hello, World!");


});


function getData() {

	// get any form data needed
	var the_data = {"data":23}


	$.post( "/build_graph", {
	  canvas_data: JSON.stringify(the_data)
	}, function(err, req, resp){
	 resp["responseJSON"]["uuid"];  
	});

}
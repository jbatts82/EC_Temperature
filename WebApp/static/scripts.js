// helper_script.js


var Client_Model = {
    "graph_lines": {"ch1": true, "ch2": false, "ch3": false, "ch4": false, "heater": false, "light": true, "fan": false},
    "web_control": {
    "heater_req": false,
    "heater_state": false,
    "fan_req": false,
    "fan_state": false}
};

var Server_Model = {
    "graph_lines": {"ch1": true, "ch2": false, "ch3": false, "ch4": false, "heater": false, "light": true, "fan": false},
    "web_control": {
    "heater_req": false,
    "heater_state": false,
    "fan_req": false,
    "fan_state": false}
};


// after page loads
$(document).ready(function() {
    get_server_model();
    update_client_model();
    draw_graph_lines();
    set_web_control();
});




function get_server_model(){
    return Server_Model;
}

function update_client_model() {
    update_web_control();
    update_graph_lines();
	
}

function update_web_control() {
    get_fan_override();
    get_heater_override();
}

function update_graph_lines() {
    get_graph_lines();
}

function draw_graph_lines() {
    set_graph_lines();
}



// Data Getter functions for HTML pages
function get_fan_override() {

    if ($("#is_fan_override").is(":checked")) {
        Client_Model.web_control.fan_req = true;
    }
    else {
        Client_Model.web_control.fan_req = false;
    }

    if ($("#fan_override_state").is(":checked")) {
        Client_Model.web_control.fan_state = true;
    }
    else {
         Client_Model.web_control.fan_state = false;
    }

}

function get_heater_override() {
    if ($("#is_heater_override").is(":checked")) {
        Client_Model.web_control.heater_req = true;
    }
    else {
        Client_Model.web_control.heater_req = false;
    }

    if ($("#heater_override_state").is(":checked")) {
        Client_Model.web_control.heater_state = false;
    }
    else {
        Client_Model.web_control.heater_state = false;
    }
}


function get_graph_lines() {

	if ($("#show_heater").is(":checked")) {
		Client_Model.graph_lines.heater = true;
	}
	else {
		Client_Model.graph_lines.heater= false;
	}

	if ($("#show_light").is(":checked")) {
		Client_Model.graph_lines.light= true;
	}
	else {
		Client_Model.graph_lines.light = false;
	}

	if ($("#show_fan").is(":checked")) {
		Client_Model.graph_lines.fan = true;
	}
	else {
		Client_Model.graph_lines.fan = false;
	}

	if ($("#show_ch1").is(":checked")) {
		Client_Model.graph_lines.ch1 = true;
	}
	else {
		Client_Model.graph_lines.ch1 = false;
	}

	if ($("#show_ch2").is(":checked")) {
		Client_Model.graph_lines.ch2 = true;
	}
	else {
		Client_Model.graph_lines.ch2 = false;
	}

	if ($("#show_ch3").is(":checked")) {
		Client_Model.graph_lines.ch3 = true;
	}
	else {
		Client_Model.graph_lines.ch3 = false;
	}

	if ($("#show_ch4").is(":checked")) {
		Client_Model.graph_lines.ch4 = true;
	}
	else {
		Client_Model.graph_lines.ch4 = false;
	}

}


function set_graph_lines() {
	$.post( "/set_graph_lines", {
	  graph_data: JSON.stringify(Client_Model.graph_lines)
	}, function(resp){

		var the_64data = JSON.parse(resp);

		if (the_64data.error === true)
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

		if (the_resp.error === true)
		{
			alert("Error");
		}
		else
		{

		}
	});
}

function set_web_control(){
    send_data("/update_model", Client_Model.web_control);
}
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
    update_client_model(Server_Model);
    draw_graph_lines();
    set_page_elements();
});


function update_model() {
	get_page_elements();
	send_client_model();
}

function update_client_model(new_model) {
    Client_Model = new_model;
}

function update_client_model_page() {
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
    send_graph_data();
}


function send_graph_data() {
	$.post( "/set_graph_data", {
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

function get_server_model(){
	$.post( "/get_server_model", {
	  "cmd": "GET_SERVER_MODEL"
	}, function(resp){

		var response = JSON.parse(resp);

		if (response.error === true)
		{

		}
		else
		{
			Server_Model = response.server_model;
			Client_Model = Server_Model;
			$("#demo").text(JSON.stringify(Server_Model));
		}
	});

}

function send_client_model(){
	$.post( "/send_client_model", {
	  "client_model": JSON.stringify(Client_Model)
	}, function(resp){

		var response = JSON.parse(resp);

		if (response.error === true)
		{

		}
		else
		{
			Server_Model = response.server_model;
			Client_Model = Server_Model;
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


function set_page_elements() {

	if (Client_Model.web_control.fan_req === true)
	{
		$("#is_fan_override").attr("checked", true);
	}
	else
	{
		$("#is_fan_override").attr("checked", false);
	}

	if (Client_Model.web_control.fan_state === true)
	{
		$("#fan_override_state").attr("checked", true);
	}
	else
	{
		$("#fan_override_state").attr("checked", false);
	}

	if (Client_Model.web_control.heater_req === true)
	{
		$("#is_heater_override").attr("checked", true);
	}
	else
	{
		$("#is_heater_override").attr("checked", false);
	}

	if (Client_Model.web_control.heater_state === true)
	{
		$("#heater_override_state").attr("checked", true);
	}
	else
	{
		$("#heater_override_state").attr("checked", false);
	}

	if (Client_Model.graph_lines.heater === true)
	{
		$("#show_heater").attr("checked", true);
	}
	else
	{
		$("#show_heater").attr("checked", false);
	}

	if (Client_Model.graph_lines.light === true)
	{
		$("#show_light").attr("checked", true);
	}
	else
	{
		$("#show_light").attr("checked", false);
	}

	if (Client_Model.graph_lines.fan === true)
	{
		$("#show_fan").attr("checked", true);
	}
	else
	{
		$("#show_fan").attr("checked", false);
	}

	if (Client_Model.graph_lines.ch1 == true)
	{
		$("#show_ch1").attr("checked", true);
	}
	else
	{
		$("#show_ch1").attr("checked", false);
	}

	if (Client_Model.graph_lines.ch2 == true)
	{
		$("#show_ch2").attr("checked", true);
	}
	else
	{
		$("#show_ch2").attr("checked", false);
	}

	if (Client_Model.graph_lines.ch3 == true)
	{
		$("#show_ch3").attr("checked", true);
	}
	else
	{
		$("#show_ch3").attr("checked", false);
	}

	if (Client_Model.graph_lines.ch4 == true)
	{
		$("#show_ch4").attr("checked", true);
	}
	else
	{
		$("#show_ch4").attr("checked", false);
	}
}


function get_page_elements() {
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
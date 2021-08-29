// helper_script.js

alert("Script Called");

Client_Model = {};
Server_Model = {};

// after page loads
$(document).ready(function() {
    get_server_model();
   // $("#demohi").text(JSON.stringify(window.Client_Model));
    //set_page_elements();
    //draw_graph_lines();
   
});


function get_server_model(){
	$.post( "/get_server_model", {
	  "cmd": "GET_SERVER_MODEL"
	}, function(resp){

		var response = JSON.parse(resp);

		if (response.error === true)
		{
			alert("Error");
		}
		else
		{
			set_page_elements(response.server_model);
			update_client(response.server_model);
		}
	});
}

function update_client(new_model) {
	
	window.Client_Model = new_model;


}

function update_model() {
	get_page_elements();
	send_client_model();
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
			update_client(Server_Model);
		}
	});
}



function set_page_elements(Client_Model) {

	

	if (Client_Model.web_control.fan_req)
	{
		$("#is_fan_override").attr("checked", true);
	}
	else
	{
		$("#is_fan_override").attr("checked", false);
	}

	if (Client_Model.web_control.fan_state == true)
	{
		$("#fan_override_state").attr("checked", true);
	}
	else
	{
		$("#fan_override_state").attr("checked", false);
	}

	if (Client_Model.web_control.heater_req == true)
	{
		$("#is_heater_override").attr("checked", true);
	}
	else
	{
		$("#is_heater_override").attr("checked", false);
	}

	if (Client_Model.web_control.heater_state == true)
	{
		$("#heater_override_state").attr("checked", true);
	}
	else
	{
		$("#heater_override_state").attr("checked", false);
	}

	if (Client_Model.graph_lines.heater == true)
	{
		$("#show_heater").attr("checked", true);
	}
	else
	{
		$("#show_heater").attr("checked", false);
	}

	if (Client_Model.graph_lines.light == true)
	{
		$("#show_light").attr("checked", true);
	}
	else
	{
		$("#show_light").attr("checked", false);
	}

	if (Client_Model.graph_lines.fan == true)
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
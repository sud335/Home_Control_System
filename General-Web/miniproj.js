$(document).ready(function() {
	$('.diftabs').hide(); 
	$('#home').show();
	var linkt = window.location.href;
	linkt = linkt.split("/");
	document.getElementById("videoLink").href = "http://"+linkt[2]+":8091"
	$.get('/cgi-bin/temperature.py',{},function(data){
		//alert(JSON.stringify(data));
		var gets = data;
		$("#temp").html("<b>"+gets["Temp"]+"&deg;"+"C</b>");
		$("#humid").html("<b>"+gets["Humidity"]+" %</b>");
	});


});

var i=0;
function makeCall(vals)
{
	if (i==0)
	{
	send = {"keyword":JSON.stringify(vals)};
	$.get('/cgi-bin/on.py',send, function(data){});
	i=1;
	}
	else if(i==1 ){
	send = {"keyword":JSON.stringify(vals)};
	$.get('/cgi-bin/off.py',send, function(data){});	
	i=0;
	}			

}


function performCall()
{
	if (i==0)
	{
	$("#fanDiv").addClass("fan");
	send = {"keyword":"on"};
	$.get('/cgi-bin/fanon.py',send, function(data){});
	i=1;	
	}
	else if(i==1)
	{

	$("#fanDiv").removeClass("fan");
	//$(".fan").css("animation-name", "none");
	send = {"keyword":"off"};
	$.get('/cgi-bin/fanon.py',send, function(data){});
	i=0;
	}
}

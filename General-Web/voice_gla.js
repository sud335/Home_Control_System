var disc = ["switch","led","leds"];

var operation = ["on","off"];
var map = {"green":1,"yellow":2,"red":3};

var color = ["green","red","yellow"];
var link = "";

function makeCall(text)
{

var op="";
var colors=[];
var mode="";
var send = {"keyword":{}};

if(text.indexOf(" ")>=0)
{
console.log(text);
if (text.indexOf("off")>=0)
{
console.log(JSON.stringify(send));
if(text.indexOf("fan")>=0)
{	var send={};
	send["keyword"]="off";
	$.get(link+"/cgi-bin/fanon.py",send,function(data){});
}
else{
$.post(link+"/cgi-bin/off.py",send,function(data){});
}
}
if (text.indexOf("on")>=0)
{
mode ="on";
for (i=0;i<color.length;i++)
{
//console.log(color[i]);
if (text.indexOf(color[i])>=0)
colors=colors.concat(map[color[i]]);
}

if (colors.length==1)
{
send["keyword"]["one"] =colors;
}

else if(colors.length==2)
{
send["keyword"]["two"] = colors;
}

else if (colors.length==0 || color.length==3)
{
send["keyword"]["three"] = [];
}

if (text.indexOf("wave")>0)
{
send ={"keyword":{}};
send["keyword"]["wave"]=[];
}
console.log(JSON.stringify(send));
console.log(JSON.stringify(Object.keys(send)));
if (Object.keys(send).length>0)
{
	if(text.indexOf("fan")>=0)
	{
		var send={};

		send["keyword"]="on";
		$.get(link+"/cgi-bin/fanon.py",send,function(data){});
	}
	else
	{

send["keyword"]=JSON.stringify(send["keyword"]);
console.log(JSON.stringify(send));
$.get(link+"/cgi-bin/on.py",send,function(data){});
}
}
}


}
}

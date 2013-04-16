function sendPost(value){
    
    $.post("/command/", {command:value});
}

function action(name){
    var code=$('textarea[name=\"'+name+'\"]');
    $.post("/action/", {actionType:name, actionCode:code});
}

function panel(value){
    $.post("/command/", {command:value, parameter:$('#voltage').val(), quantity:$('#quantity').val()});}


function addPoints(value){
    $.post("addPoints/", {command:value});
}

function conveyor(value){
    $.post("/command/", {command:value, parameter:$('#conveyor').val()});
}

function pusher(value){
    $.post("/command/", {command:value, parameter:$('#pusher').val()});
}

function solderingPower(value){
    $.post("/command/", {command:value, parameter:$('#solderingPower').val()});
}

function solettes(value){
    $.post("/command/", {command:value, parameter:$('#solettes').val()});
}

function pick(value){
    $.post("/command/", {command:value, parameter:$('#pick').val()});
}

function tabbing(value){
    $.post("/command/", {command:value, parameter:$('#tabbing').val()});
}

function sendValue(value){
    var inputId="input#"+value;
    $.post("/tinyGParameter/", {command:value, parameter:$(inputId).val()});
}

function sendPanelValue(value){
    var inputId="input#"+value;
    $.post("/panelParameter/", {command:value, parameter:$(inputId).val()});
}

function updateFactoryState(value){
    var inputId="input#"+value;
    $.post("/factoryState/", {command:value, parameter:$(inputId).val()});
}
function deleteCommand(value){
    console.log("deleting command"+value);
    $.post("/deleteCommand/", {command:value});
}

function deletePoint(value){
    console.log("deleting point "+value);
    $.post("/deletePoint/", {point:value});
}

function deleteAllPoints()
{
    console.log("deleting all points");
    $.post("/deleteAllPoints/");
}

/*
(function pendingCommandsPoll(){
    var activeTab=$('#tabs').tabs('option', 'active');
    if(activeTab==3)  //only look for points if we're displaying the latest points
	{
    $.ajax({
	    url: "http://testing.solarpocketFactory.com/pendingPoints/", 
	       dataType:' json',
		success: function(data){
		var pendingCommands="";
		for(var i=0;i<data.length;i++){
		    pendingCommands+="\n<div class='command-list'><span class='command-type'>"+data[i].fields["pointType"]+"</span><span class='point-distance'>Position: "+data[i].fields["position"]+"</span><span class='point-distance'>Remaining distance: "+data[i].fields["remainingDistance"]+"</span><button class='command-button' onClick=\"deletePoint("+data[i].pk+")\">X</button></div>";
		    }
		$("div#jobs").html(pendingCommands);
	    }, dataType: "json", complete: pendingCommandsPoll, timeout: 5000 });
	}
})();


//couldn't get this function to trigger on a UI event, will have to come back to it
$("#tabs").tabs({activate: function(event, ui){
	
    var activeTab=$('#tabs').tabs('option', 'active');
    console.log(activeTab);
    if(activeTab==3)
	pendingCommandsPoll();
	} });
*/

(function pendingCommandsPoll(){
    $.ajax({
	    url: "http://internal.solarpocketFactory.com/pendingPoints/", 
	       dataType:' json',
		success: function(data){
		var pendingCommands="";
		var min=1000;
		var max=-1000;
		for(var i=0;i<data.length;i++){
		    data[i].fields["position"]=parseFloat(data[i].fields["position"]);
		    if(data[i].fields["position"]<min)
			min=data[i].fields["position"];
		    if(data[i].fields["position"]>max)
			max=data[i].fields["position"];
		}
		$("canvas").clearCanvas();
		    drawLegend();
		var pendingCommands="";
		for(var i=0;i<data.length;i++){
		    var color=""
		    if(data[i].fields["pointType"]=="start")
			color="#00FF00";
		    if(data[i].fields["pointType"]=="end")
			color="#FF0000";
		    if(data[i].fields["pointType"]=="placeSolette")
			color="#FFFF00";
		    if(data[i].fields["pointType"]=="tab")
			color="#0000FF";
		    if(data[i].fields["pointType"]=="solder")
			color="#FF00FF";

		    var position=(max-data[i].fields["position"])*$("canvas#points").width()/(max-min);
		    $("canvas#points").drawEllipse({
			    fillStyle: color,
				x: position, y: 100,
				width: 5, height: 5
				});
		    pendingCommands+="\n<div class='command-list'><span class='command-type'>"+data[i].fields["pointType"]+"</span><span class='point-distance'>Position: "+data[i].fields["position"]+"</span><span class='point-distance'>Remaining distance: "+data[i].fields["remainingDistance"]+"</span><button class='command-button' onClick=\"deletePoint("+data[i].pk+");\">X</button></div>";
	    }
		$("div#jobs").html(pendingCommands);
	    }, dataType: "json", complete: pendingCommandsPoll, timeout: 5000 });
})();


function drawLegend()
{
    $("canvas#points").drawText({
	    fillStyle: "#00FF00",
		strokeWidth: 2,
		x: 400, y: 250,
		font: "18pt Verdana, sans-serif",
		text: "start"
		});

    $("canvas#points").drawText({
	    fillStyle: "#FF0000",
		strokeWidth: 2,
		x: 400, y: 270,
		font: "18pt Verdana, sans-serif",
		text: "end"
		});
    $("canvas#points").drawText({
	    fillStyle: "#FFFF00",
		strokeWidth: 2,
		x: 400, y: 290,
		font: "18pt Verdana, sans-serif",
		text: "placeSolette"
		});
    $("canvas#points").drawText({
	    fillStyle: "#0000FF",
		strokeWidth: 2,
		x: 400, y: 310,
		font: "18pt Verdana, sans-serif",
		text: "tab"
		});
    $("canvas#points").drawText({
	    fillStyle: "#FF00FF",
		strokeWidth: 2,
		x: 400, y: 330,
		font: "18pt Verdana, sans-serif",
		text: "solder"
		});
}
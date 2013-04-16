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
	    url: "http://testing.solarpocketFactory.com/pendingPoints/", 
	       dataType:' json',
		success: function(data){
		var pendingCommands="";
		for(var i=0;i<data.length;i++){
		    pendingCommands+="\n<div class='command-list'><span class='command-type'>"+data[i].fields["pointType"]+"</span><span class='point-distance'>Position: "+data[i].fields["position"]+"</span><span class='point-distance'>Remaining distance: "+data[i].fields["remainingDistance"]+"</span><button class='command-button' onClick=\"deletePoint("+data[i].pk+");\">X</button></div>";
		    }
		$("div#jobs").html(pendingCommands);
	    }, dataType: "json", complete: pendingCommandsPoll, timeout: 5000 });
})();



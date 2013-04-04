from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from command.models import Command
from factoryState.models import FactoryState
from panel.models import Panel
from django.utils import timezone
from django.core import serializers
from panel.models import Panel
import os

def command(request):
        if request.method == 'POST':
		_command=request.POST.get('command', 'boo')
		_parameter=request.POST.get('parameter',0)
		_quantity=request.POST.get('quantity',0)
		myCommand = Command(command=_command, statusTimeStamp=timezone.now(), parameter=_parameter, quantity=_quantity, status='queued', commandTimeStamp=timezone.now())
		myCommand.json=jsonTranslation(myCommand)
                myCommand.save()
                return HttpResponse(myCommand.json)
	else:
		return HttpResponse("bite me")

def deleteCommand(request):
        if request.method == 'POST':
		_command=request.POST.get('command', 'boo')
		command=Command.objects.filter(pk=_command)
		command.delete()
	return HttpResponse("ok")


def jsonTranslation(_command):
	if FactoryState.objects.exists():  #assuming we have a factoryState object, pass it to the appropriate json template, render the template, and pass it back, to get stored along with the command
		factoryState=FactoryState.objects.get(id=1)
		if Panel.objects.exists():
			panel=Panel.objects.get(id=1)
			if _command.command.find(":")==-1:  #this is a hardcoded command
				jsonString=render_to_string(_command.command + ".html", {'command': _command, 'factoryState' : factoryState, 'panel' : panel})
			elif _command.command.find("action")!=-1:
				jsonString=render_to_string(_command.command[:_command.command.find(":")] + "/"+_command.command[_command.command.find(":")+1:]+".html", {'command': _command, 'factoryState' : factoryState, 'panel' : panel})								
			else:  #it's a custom button, extract the folder and render that sucker
				jsonString=render_to_string(_command.command[:_command.command.find(":")] + "/"+_command.command[_command.command.find(":")+1:], {'command': _command, 'factoryState' : factoryState, 'panel' : panel})				
		else:
			jsonString=""
	else:
		jsonString=""
	return jsonString


def renderAction(request):
        if request.method == 'POST':
		action=request.POST.get('actionType')
#		action=request.POST.values()
		action="actions:"+action
		
		myCommand = Command(command=action, statusTimeStamp=timezone.now(), parameter="", quantity=0, status='queued', commandTimeStamp=timezone.now())
		myCommand.json=jsonTranslation(myCommand)
#		return HttpResponse(action)
		return HttpResponse(myCommand.json)
	else:
		return HttpResponse("no joy")


def tinyGParameter(request):
        if request.method == 'POST':
		_command=request.POST.get('command', 'boo')
		_parameter=request.POST.get('parameter',0)
		factoryState=FactoryState.objects.get(id=1)
		if _command.find('var_')!=-1:
			setattr(factoryState, _command, _parameter)
			_command=_command[4:]
			factoryState.save()
		myCommand = Command(command=_command, statusTimeStamp=timezone.now(), quantity=0,parameter=_parameter, status='queued', commandTimeStamp=timezone.now())
		myCommand.json=render_to_string("parameter.html", {'command': myCommand})
                myCommand.save()
                return HttpResponse("parameter set")
	else:
		return HttpResponse("poo")

def factoryState(request):
        if request.method == 'POST':
		_command=request.POST.get('command', 'boo')
		_parameter=request.POST.get('parameter',0)
		factoryState=FactoryState.objects.get(id=1)
		setattr(factoryState, _command, _parameter)
		factoryState.save()
		return HttpResponse("factory settings updated")
	else:
		return HttpResponse("poo")


def startup(request):
	if FactoryState.objects.exists():  #assuming we have a factoryState object, pass it to the appropriate json template, render the template, and pass it back, to get stored along with the command
		factoryState=FactoryState.objects.get(id=1)
	return render(request, 'startup.html', {'factoryState' : factoryState})

def pendingCommands(request):
	pendingCommands=serializers.serialize("json",Command.objects.all().filter(status='queued').order_by('-commandTimeStamp'))
	return HttpResponse(pendingCommands);

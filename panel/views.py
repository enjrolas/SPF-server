from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from command.models import Command
from factoryState.models import FactoryState
from panel.models import Panel
from django.utils import timezone
from django.core import serializers

def panelParameter(request):
        if request.method == 'POST':
		_command=request.POST.get('command', 'boo')
		_parameter=request.POST.get('parameter',0)
                panel=Panel.objects.get(id=1)
                setattr(panel, _command, _parameter)
                panel.save()
                return HttpResponse("panel settings updated")
	else:
		return HttpResponse("poo")

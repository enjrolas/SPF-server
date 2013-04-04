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
from action.models import Action
import os

def interface(request):
    """assuming we have a factoryState object, pass it to the appropriate json template, render the template, and pass it back, to get stored along with the command"""
    factoryState=FactoryState.objects.get(id=1)
    panel=Panel.objects.get(id=1)
    actions=Action.objects.all()
    programs=os.listdir("/home/japhy/solarPocketFactory/templates/programs")
    musics=os.listdir("/home/japhy/solarPocketFactory/templates/music")
    return render(request, 'interface.html', {'factoryState' : factoryState, 'panel' :panel, 'programs' : programs, 'musics': musics, 'actions' :actions})


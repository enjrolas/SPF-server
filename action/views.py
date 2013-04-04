from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from action.models import Action

def action(request):
        if request.method == 'POST':
		_actionType=request.POST.get('actionType',0)
		_actionCode=request.POST.get('actionCode',0)
                existingAction=Action.objects.filter(actionType=_actionType)
		if len(existingAction)==0:  # the action isn't in the DB
                    myAction=Action(actionType=_actionType, actionCode=_actionCode)
                else:
                    myAction=Action.objects.get(actionType=_actionType)
                    myAction.actionCode=_actionCode
                myAction.save()


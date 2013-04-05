from django.http import HttpResponse
from django.core import serializers
from point.models import Point
import os

def pendingPoints(request):
	pendingCommands=serializers.serialize("json",Point.objects.all().filter(status='queued').order_by('-commandTimeStamp'))
	return HttpResponse(pendingCommands);

def deletePoint(request):
        if request.method == 'POST':
		_point=request.POST.get('point', 0)
		point=Point.objects.filter(pk=_point)
		point.delete()
	return HttpResponse("ok")


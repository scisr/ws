# Create your views here.

from main.models import Event
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader

def next_event(request):
    next_event = Event.objects.get()
    return render_to_response('scisr.html', {'next_event' : next_event})

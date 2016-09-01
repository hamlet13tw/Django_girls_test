#trips/views.py
from datetime import datetime
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def hello_world(request):
	#return HttpResponse("This will print Hello World !!")
	return render(request, 'hello_world.html', {
	'current_time': str(datetime.now()),
	})
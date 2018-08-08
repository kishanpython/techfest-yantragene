from django.shortcuts import render
from events.models import Events,Participant

def about_us(request):
	
	context={
		'events':Events.objects.all().count(),
		'team_participated':Participant.objects.all().count(),
		'prize':'1,00,000',
	}

	return render(request,'about.html',context)

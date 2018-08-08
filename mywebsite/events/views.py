from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import  Branch,Events,Coordinator,Participant

# Create your views here.

def branch(request):
	branch_all=Branch.objects.all()
	event_all=Events.objects.all()
     
     # ALL ELEMENTS FROM THE DATABASE TAKEN BY MODULE

	outer_event=dict()
	for b in branch_all:
		e=event_all.filter(branch=b)
		outer_event[b]=e

	context={
	    	 'outer_event':outer_event,
	    	 'branch_all':branch_all
	        }
	return render(request,'events.html',context)



def event_details(request,id=None):
	coord = Coordinator.objects.filter(event_id=id)
	#eve = Events.objects.get(id=id)
	events = get_object_or_404(Events,id=id)
	page=events.event.lower()
	page='events/'+page+'.html'
	context = {
	      'eve':events.event.upper(),
	      'events':events,
	     'coord':coord
	}

	return render(request,page,context)


####.....REGISTERATION  FOR EVENTS.....##### 


def register_view(request):

	team_name = request.GET['team_name']
	member2 = request.GET['member2']
	member3 = request.GET['member3']
	member4 = request.GET['member4']
	member5 = request.GET['member5']
	event_id = request.GET['event_id']
	profile_id = request.GET['profile_id']
	events_name = request.GET['events_name']

	t=Participant.objects.filter(team_name=team_name)
	if len(t):
		return render(request,'events.html',{'msg':'Team name already taken'})

	t=Participant.objects.filter(profile=profile_id, events_name=events_name)
	if len(t):
		return render(request,'events.html',{'msg':'You are already participated in this event'})
	part=Participant(

		team_name=team_name,
		events_name=events_name,
		member2=member2,
		member3=member3,
		member4=member4,
		member5=member5,
		events_id=event_id,
		profile_id=profile_id,


		)
	part.save()
	return HttpResponseRedirect(reverse('events:events'))
	



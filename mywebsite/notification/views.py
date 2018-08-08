from django.shortcuts import render
from .models import Notify


def notice(request):
	data = Notify.objects.all()
	note = {
		"note_number": data
    }
	return render(request,'notify.html',note)
	


	
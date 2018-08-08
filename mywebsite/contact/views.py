from django.shortcuts import render
from .models import Feedback
from .forms import Feedbackform

# Create your views here.

def contact(request):
	form=Feedbackform()
	return render(request,'contact.html',{'form':form})

def feed(request):

	name=request.GET['name']
	email=request.GET['email']
	feed=request.GET['feed']

	f=Feedback(

		name=name,
		email=email,
		feed=feed,

		)
	f.save()

	form=Feedbackform()
	return render(request,'contact.html',{'form':forms})


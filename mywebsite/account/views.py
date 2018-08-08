from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
from django.core.urlresolvers import reverse
from events.models import Participant
from django.contrib.auth import (
   
   authenticate,
   login,
   logout,
	
	)

def register_view(request):
	if request.method=='POST':
		firstname=request.POST['fname']
		lastname=request.POST['lname']
		username=request.POST['uname']
		password=request.POST['password']
		cpassword=request.POST['cpassword']
		email=request.POST['email']
		mobile=request.POST['mobile']
	    
	   ####....VALIDATIONS.....######

		t=User.objects.filter(username=username)
		if len(t):
			return render(request,'account/register.html',{'msg':'Username already taken'})
	    
		e=User.objects.filter(email=email)
		if len(e):
			return render(request,'account/register.html',{'msg':'Email id not correct'})
	   
		if len(mobile)!=10:
			return render(request,'account/register.html',{'msg':'Enter correct mobile number'})
	    
		m=Profile.objects.filter(mobile=mobile)
		if len(m):
			return render(request,'account/register.html',{'mag':'Mobile number already register'})

		if password!=cpassword:
	   		return render(requets,'account/register.html',{'msg':'Password and Confirm password not matched'})

	    ####....CREATE USER OBJECT ......#### 	
	    
		user,create=User.objects.get_or_create(

				first_name=firstname,
				last_name=lastname,
				username=username,
				email=email,
			
		)

		user.set_password(password)
		user.save()
		pro=Profile(user=user, mobile=mobile)
		pro.save()

		return HttpResponseRedirect(reverse('account:login'))
	else:
		return render(request,'account/register.html')	



def login_view(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']

		try:
			user=authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return render(request,'home/home.html')

			else:
				return render(request,'account/login.html',{'msg':'Wrong Username or Password'})
		except:
			return render(request,'account/login.html',{'msg':'Error in login'})
	else:
		return render(request,'account/login.html')



def logout_view(request):
	logout(request)
	return render(request,'home/home.html')



def profile_view(request,id=None):
	participant = Participant.objects.filter(profile=id)
	context={
      'participant':participant,
      'length':len(participant)
	}
	return render(request,'account/profile.html',context)




def delete_event(request, id=None, proid=None):		
	try:
		p = Participant.objects.get(id=id)
		p.delete()
	except:
		pass
	finally:
		return HttpResponseRedirect(reverse('account:profile', kwargs={'id': proid }))

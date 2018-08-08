from django.db import models
from account.models import Profile

class Branch(models.Model):
	branch=models.CharField(max_length=200)
	bimage=models.ImageField(null=True)
	def __str__(self):
		return self.branch

class Events(models.Model):
	event=models.CharField(max_length=200)
	branch=models.ForeignKey(Branch)
	def __str__(self):
		return self.event
		
class Coordinator(models.Model):
	event=models.ForeignKey(Events)
	cname=models.CharField(max_length=200)
	cmobile=models.IntegerField(null=True)
	cimage=models.ImageField(null=True)
	cemail=models.EmailField(max_length=200,null=True)
	
	def __str__(self):
		return self.cname

class Participant(models.Model):
	events = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	team_name = models.CharField(max_length=30,  null=True)
	events_name = models.CharField(max_length=30,  null=True)
	member2 = models.CharField(max_length=50, null=True)
	member3 = models.CharField(max_length=50,  null=True)
	member4 = models.CharField(max_length=50,  null=True)
	member5 = models.CharField(max_length=50,  null=True)

	def __str__(self):
		return self.team_name





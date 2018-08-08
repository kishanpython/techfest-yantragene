from django.db import models

class Notify(models.Model):
	p1=models.CharField(max_length=300)
	p2=models.CharField(max_length=300)
	p3=models.CharField(max_length=300)
	p4=models.CharField(max_length=300)
	def __str__(self):
		return self.p1
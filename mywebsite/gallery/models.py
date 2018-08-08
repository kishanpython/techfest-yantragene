from django.db import models

# Create your models here.

class gallery(models.Model):
	imgid=models.CharField(max_length=4)
	image=models.ImageField(upload_to='images/gallery', blank=True)

	def __str__(self):
		return self.imgid
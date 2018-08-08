from django.shortcuts import render
from .models import gallery

# Create your views here.


def gallery_view(request):
	images=gallery.objects.all()
	return render(request,'gallery.html',{'images':images})
from django.conf.urls import url
from . import views

urlpatterns=[

		url(r'^$',views.gallery_view,name='gallery'),


]
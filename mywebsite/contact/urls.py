from django.conf.urls import url
from . import views

urlpatterns=[

		url(r'^$', views.contact, name="contact"),
		url(r'^feed/$', views.feed , name="feed"),
		
]
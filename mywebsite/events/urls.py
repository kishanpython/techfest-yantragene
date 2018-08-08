from django.conf.urls import url
from . import views

urlpatterns=[

		url(r'^$', views.branch, name="events"),
		url(r'^details/(?P<id>\d+)/$', views.event_details , name='details'),
		url(r'^register/$', views.register_view , name="register"),
		
]


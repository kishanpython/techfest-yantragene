from django.contrib import admin
from . models import Branch,Events,Coordinator,Participant

class Adminbranch(admin.ModelAdmin):
	list_display=['branch','bimage']

class Adminevents(admin.ModelAdmin):
	list_display=['event']

class Admincoord(admin.ModelAdmin):
	list_display=['cname','cemail','cimage']

class Adminparticipant(admin.ModelAdmin):
	list_display=['team_name','events_name','member2','member3','member4','member5']

admin.site.register(Branch,Adminbranch)
admin.site.register(Events,Adminevents)
admin.site.register(Coordinator,Admincoord)
admin.site.register(Participant,Adminparticipant)
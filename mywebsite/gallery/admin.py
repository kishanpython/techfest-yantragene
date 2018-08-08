from django.contrib import admin

from .models import gallery

class Admingallery(admin.ModelAdmin):
	list_display = ['imgid', 'image']

admin.site.register(gallery, Admingallery)
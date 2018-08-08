from django import forms
from .models import Notify

class Notes_reg(forms.ModelForm):
	class Meta:
		model=Notify
		fields=[
		'p1',
		'p2',
		'p3',
		'p4',
		'p5'

    ]
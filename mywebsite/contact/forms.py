from django import forms

class Feedbackform(forms.Form):

	name=forms.CharField(label='Your Name:',
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'Name Please!'

			}
		)
		
	)


	email=forms.CharField(label="Your Email Id:",
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'Email Id '

			}
		)
		
	)


	feed=forms.CharField(label="Write your feed:",
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'Feedback'

			}
		)
		
	)

		



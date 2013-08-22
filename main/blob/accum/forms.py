from django import forms

class MediaForm(forms.Form):
	file = forms.FileField(
			label='Select a file',
			help_text='max. 42 mb'
		)
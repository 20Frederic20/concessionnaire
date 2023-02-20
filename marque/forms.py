from django import forms
from voiture.models import Marque

class MarqueForm(forms.ModelForm):

	class Meta:

		model = Marque

		fields = '__all__'

		widgets = {
		    'name': forms.TextInput(attrs={
		        'class': 'form-control',
		        'placeholder': 'lorem ipsum',
		    }),
		}

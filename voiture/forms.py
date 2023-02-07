from django import forms
from .models import Marque, Voiture

class VoitureForm(forms.ModelForm):

	class Meta:

		model = Voiture

		fields = '__all__'

		widgets = {
		    'name': forms.TextInput(attrs={
		        'class': 'form-control',
		        'placeholder': 'lorem ipsum',
		    }),

		    'price': forms.NumberInput(
		    	attrs={
		    		'class': 'form-control',
		    		'placeholder': '123457.90',
		    	}
		    ),

		    'marque': forms.Select(
		    	attrs={
		    		'class': 'form-control',
		    	}
		    ),

		    'image': forms.FileInput(
		    	attrs={
		    		'class': 'form-control',
		    	}
		    ),
		}

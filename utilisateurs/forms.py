from django import forms
from django.contrib.auth.models import User
from .models import Profile


# Classe permettant de definir réellement les inputs de type date sur date
class DateInput(forms.DateInput):
	input_type='date'


# Formulaire de modifications des infos de l'utilisateur
class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')
		widgets = {

			'first_name': forms.TextInput(
		    	attrs={
		    		'class': 'form-control first_name',
		    	}
		    ),
		    'last_name': forms.TextInput(
		    	attrs={
		    		'class': 'form-control last_name',
		    	}
		    ),
		    'email': forms.EmailInput(attrs={
		        'class': 'form-control email',
		    }),
		}


# Formulaire de profil utilisateur		
class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('date_of_birth', 'photo')
		widgets = {

			'photo': forms.FileInput(
		    	attrs={
		    		'class': 'form-control',
		    	}
		    ),
		    'date_of_birth': DateInput(
		    	attrs={
		        	'class': 'form-control',
		    }),
		}


# Formulaire de connexion utilisateur
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',}))


# Formulaire d'inscription d'utilisateur
class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'name': 'password',}))
	password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control','id': 'confirm_password', 'name': 'confirm_password',}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')
		widgets = {

			'username': forms.TextInput(
		    	attrs={
		    		'class': 'form-control',
					'id': 'username',
					'name': 'username',
		    	}
		    ),
		    'first_name': forms.TextInput(
		    	attrs={
		    		'class': 'form-control',
					'id': 'first_name',
					'name': 'firstname',
		    	}
		    ),
		    'email': forms.EmailInput(attrs={
		        'class': 'form-control',
				'id': 'email',
				'name': 'email',
		    }),
		}

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']
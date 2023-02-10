from django import forms
from django.contrib.auth.models import User
from .models import Profile


class DateInput(forms.DateInput):
	input_type='date'


class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')
		widgets = {

			'first_name': forms.TextInput(
		    	attrs={
		    		'class': 'form-control',
		    	}
		    ),
		    'last_name': forms.TextInput(
		    	attrs={
		    		'class': 'form-control',
		    	}
		    ),
		    'email': forms.EmailInput(attrs={
		        'class': 'form-control',
		    }),
		}

		
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


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',}))


class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',}))
	password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control',}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')
		widgets = {

			'username': forms.TextInput(
		    	attrs={
		    		'class': 'form-control',
		    	}
		    ),
		    'first_name': forms.TextInput(
		    	attrs={
		    		'class': 'form-control',
		    	}
		    ),
		    'email': forms.EmailInput(attrs={
		        'class': 'form-control',
		    }),
		}

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']
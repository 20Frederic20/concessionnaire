from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

# Vue ddu dashboard définie sous forme de fonction
@login_required
def dashboard(request):
	profile = Profile.objects.get(user=request.user)
	return render(request,'Utilisateurs/dashboard.html', {'profile': profile})


# Vue d'édition des informations de l'utilisateur
@login_required
def edit(request):
	if request.method == 'POST':
		#Cette partie appelle le formulaire d'edition de l'utilisateur avec pour inistance l'user actuellemnt connecté
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request, 'Utilisateurs/edit.html', {'user_form': user_form, 'profile_form': profile_form})

# Vue de creation d'utilisateur
class RegistrationView(View):
	form_class = UserRegistrationForm
	template_name = 'utilisateurs/register.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {'form': self.form_class})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)

			user.set_password(form.cleaned_data['password'])

			user.save()

			Profile.objects.create(user=user)

			return redirect('utilisateurs:register_done')
		return render(request, self.template_name, {'form': self.form_class})


# Vue de redirection de l'utilisation une fois le compte proprement créé.
class RegistrationDone(View):
	template_name='utilisateurs/register_done.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)
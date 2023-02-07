from django.shortcuts import render
from .models import Marque, Voiture
from .forms import VoitureForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
# Create your views here.


class VoitureList(ListView):
	model = Voiture
	template_name = 'Voiture/list.html'
	context_object_name = 'voitures'


class VoitureDetail(DetailView):
	model = Voiture
	template_name = 'Voiture/detail.html'
	context_object_name = 'voiture'
		

class VoitureAdd(CreateView):		
	model = Voiture
	template_name = 'Voiture/add.html'
	form_class = VoitureForm
	success_url = reverse_lazy('voiture:list')


class VoitureUpdate(UpdateView):		
	model = Voiture
	template_name = 'Voiture/add.html'
	form_class = VoitureForm
	success_url = reverse_lazy('voiture:list')


class VoitureDelete(DeleteView):		
	model = Voiture
	success_url = reverse_lazy('voiture:list')
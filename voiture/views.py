from django.shortcuts import render
from .models import Marque, Voiture
from .forms import VoitureForm
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView,DeleteView
# Create your views here.


class VoitureView(ListView):
	template_name='Voiture/index.html'
	marques = Marque.objects.all()
	voitures = Voiture.objects.all()[:5]

	def get(self, request):
		return render(request, self.template_name, {'marques': self.marques, 'voitures': self.voitures })



class VoitureList(ListView):
	template_name = 'Voiture/list.html'
	marques = Marque.objects.all()
	voitures = Voiture.objects.all()

	def get(self, request):
		return render(request, self.template_name, {'marques': self.marques, 'voitures': self.voitures })


class VoitureDetail(DetailView):
	template_name = 'Voiture/detail.html'
	marques = Marque.objects.all()

	def get(self, request, *args, **kwargs):
		voiture = Voiture.objects.get(pk=self.kwargs['pk'])
		return render(request, self.template_name, {'marques': self.marques, 'voiture': voiture})
		

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
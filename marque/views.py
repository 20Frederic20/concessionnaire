from django.shortcuts import render
from voiture.models import Marque, Voiture
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView,DeleteView
# Create your views here.


class MarqueDetail(DetailView):
	template_name = 'Marque/detail.html'
	marques = Marque.objects.all()
	def get(self, request, *args, **kwargs):
		voitures = Voiture.objects.filter(marque=self.kwargs['pk'])
		marque_voiture = Marque.objects.get(pk=self.kwargs['pk'])
		return render(request, self.template_name, {'marques': self.marques, 'voitures': voitures, 'marque_voiture': marque_voiture})
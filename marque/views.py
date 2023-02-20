from django.shortcuts import render
from voiture.models import Marque, Voiture
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .forms import MarqueForm
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.


class MarqueDetailView(DetailView):
	template_name = 'Marque/detail.html'
	marques = Marque.objects.all()
	def get(self, request, *args, **kwargs):
		voitures = Voiture.objects.filter(marque=self.kwargs['pk'])
		marque_voiture = Marque.objects.get(pk=self.kwargs['pk'])
		return render(request, self.template_name, {'marques': self.marques, 'voitures': voitures, 'marque_voiture': marque_voiture})


class MarqueListView(ListView):
	model = Marque
	template_name = 'Marque/list.html'
	context_object_name = 'marques'


class MarqueCreateView(CreateView):
	model = Marque
	template_name = "Marque/create.html"
	form_class = MarqueForm
	success_url = reverse_lazy('marque:list')


class MarqueUpdateView(UpdateView):
	model = Marque
	template_name = "Marque/create.html"
	form_class = MarqueForm
	success_url = reverse_lazy('marque:list')


class MarqueDeleteView(DeleteView):
	model = Marque
	success_url = reverse_lazy('marque:list')
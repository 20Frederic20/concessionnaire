from django.shortcuts import render
from .models import Marque, Voiture
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import VoitureForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView,DeleteView
# Create your views here.


class VoitureView(ListView):
	template_name='Voiture/index.html'
	voitures = Voiture.objects.all()[:3]

	def get(self, request):
		return render(request, self.template_name, {'voitures': self.voitures})



class VoitureList(ListView):
	template_name = 'Voiture/list.html'
	voitures = Voiture.objects.all()
	marques = Marque.objects.all()

	def get(self, request):
		return render(request, self.template_name, {'marques': self.marques, 'voitures': self.voitures})


class VoitureDetail(DetailView):
	template_name = 'Voiture/detail.html'
	marques = Marque.objects.all()

	def get(self, request, *args, **kwargs):
		voiture = Voiture.objects.get(pk=self.kwargs['pk'])
		return render(request, self.template_name, {'marques': self.marques, 'voiture': voiture, 'nbar': 'voitures' })
		

class VoitureAdd(CreateView):		
	model = Voiture
	template_name = 'Voiture/add.html'
	form_class = VoitureForm
	success_url = reverse_lazy('voiture:list')


class VoitureUpdate(UpdateView):		
	model = Voiture
	template_name = 'Voiture/update.html'
	form_class = VoitureForm
	success_url = reverse_lazy('voiture:list')


class VoitureDelete(DeleteView):		
	model = Voiture
	success_url = reverse_lazy('voiture:list')


class VoitureAchat(LoginRequiredMixin, View):
	template_name = 'Voiture/payement.html'

	def get(self, request, *args, **kwargs):
		voiture = Voiture.objects.get(pk=self.kwargs['pk'])
		return render(request, self.template_name, {'voiture': voiture})


class AssistanceView(View):
	template_name = 'Voiture/assistance.html'

	def get(self, request):
		return render(request, self.template_name, {})

class VoitureSearchView(View):
	template_name = "Voiture/search.html"

	def get(self, request,*args, **kwargs):
		query = request.GET.get("rechercher")
		object_list = Voiture.objects.filter( Q(name__icontains=query) | Q(marque__name__icontains=query))
		return render(request, self.template_name, {'object_list': object_list})
	
	def post(self, request, *args, **kwargs):
		return render(request, self.template_name, {})

from django.shortcuts import render
from .models import Marque, Voiture
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import VoitureForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView,DeleteView

# Create your views here.

class VoitureView(ListView):
    template_name='Voiture/index.html'
    marques = Marque.objects.all()
    voitures = Voiture.objects.all()[:3]

    def get(self, request):
        return render(request, self.template_name, {'voitures': self.voitures, 'marques': self.marques,})


class ConcessionView(View):
    template_name="Voiture/concession.html"
    marques = Marque.objects.all()

    def get(self, request):
        return render(request, self.template_name, {'marques': self.marques})


class VoitureSearchView(View):
    template_name = "Voiture/search.html"
    marques = Marque.objects.all()

    def get(self, request,*args, **kwargs):
        return render(request, self.template_name, {'marques': self.marques})

    def post(self, request, *args, **kwargs):
        query = request.POST.get("rechercher")
        if query == "" or query == " ":
            object_list = None
        else :
            object_list = Voiture.objects.filter(
                Q(name__icontains=query) | Q(marque__name__icontains=query)
            )
        return render(request, self.template_name, {'object_list': object_list, 'marques': self.marques})


class AssistanceView(View):
    template_name = 'Voiture/assistance.html'
    marques = Marque.objects.all()

    def get(self, request):
        return render(request, self.template_name, {'marques': self.marques})


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
        return render(request, self.template_name, {'marques': self.marques, 'voiture': voiture})
        

class VoitureAdd(PermissionRequiredMixin, CreateView):	
    permission_required = 'voiture.add_voiture'	
    model = Voiture
    template_name = 'Voiture/add.html'
    form_class = VoitureForm
    success_url = reverse_lazy('voiture:list')


class VoitureUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'voiture.change_voiture'		
    model = Voiture
    template_name = 'Voiture/update.html'
    form_class = VoitureForm
    success_url = reverse_lazy('voiture:list')


class VoitureDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'voiture.delete_voiture'		
    model = Voiture
    success_url = reverse_lazy('voiture:list')


class VoitureAchat(LoginRequiredMixin, View):
    login_required=True
    template_name = 'Voiture/payement.html'
    marques = Marque.objects.all()

    def get(self, request, *args, **kwargs):
        voiture = Voiture.objects.get(pk=self.kwargs['pk'])
        return render(request, self.template_name, {'voiture': voiture, 'marques': self.marques})
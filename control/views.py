from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Aula
from .forms import AulaForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Aula
    template_name = 'home.html'
    ordering = ['-id']

class Checkin(DetailView):
    model = Aula
    template_name = 'checkin.html'

class AddAulaView(CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'add_aula.html'

class UpdateAulaView(UpdateView):
    model = Aula
    form_class = AulaForm
    template_name = 'update_aula.html'

class DeleteAulaView(DeleteView):
    model = Aula
    template_name = 'delete_aula.html'
    success_url = reverse_lazy('home')
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Aula
from .forms import AulaForm

class HomeView(ListView):
    model = Aula
    template_name = 'home.html'

class Checkin(DetailView):
    model = Aula
    template_name = 'checkin.html'

class AddAulaView(CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'add_aula.html'

from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Persona, Solicitud

# Create your views here.
class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'
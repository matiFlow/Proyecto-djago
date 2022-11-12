from django.shortcuts import render
from applications.Cliente.models import Cliente
from applications.Producto.models import Producto
from applications.proveedor.models import Proveedor

from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
)

# Create your views here.

from .models import Producto

class Inicio(TemplateView):
    template_name: "inicio.html"

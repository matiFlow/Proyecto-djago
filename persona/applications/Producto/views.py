from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    CreateView,
    TemplateView,
)

from .models import Producto
from .forms import ProductoForm
from django.urls import reverse_lazy



class ProductoCreateView(CreateView):
    model = Producto
    template_name = "Producto/create.html" #Aca va a llamar al temlate del producto
    form_class = ProductoForm  # Llama a la clase del formulario
    success_url = reverse_lazy('producto_app:Creacion de producto')  # si todo esta en okey, lo va a direccionar a un template dependiendo del espa

    def form_valid(self, form):
        producto = form.save(commit=False)# Se guardan los objetos con sus valores en esta variable
        producto.save()
        return super(ProductoCreateView, self).form_valid(form)


class Inicio(TemplateView):
    template_name = "inicio.html"

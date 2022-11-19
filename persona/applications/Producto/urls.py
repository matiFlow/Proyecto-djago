from django.urls import path, re_path, include
from . import views


app_name = 'producto_app' #Espacio de nombres del producto

urlpatterns = [
    path(
        'create/',
        views.ProductoCreateView.as_view(), #Si encuentra alguna coincidencia del nombre lo va a reedirigir a un template
        name='Creacion de producto' #Aca se escribe el noimbre
    ),
]
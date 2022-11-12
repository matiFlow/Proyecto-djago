from django.db import models
from applications.Producto.models import Producto

# Create your models here.

class Cliente(models.Model):
    """campos"""
    carrito = models.ManyToManyField(Producto)
    nombre = models.CharField("Nombre del cliente", max_length=50)
    apellido = models.CharField("Apellido del cliente", max_length=50)
    telefono = models.IntegerField("Telefono del cliente")
    dni = models.IntegerField("Dni del cliente")

    class Meta:
        "Permite agregar informacion al modelo Cliente"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self) -> str:
        "Representacion de cada registro de Cliente"
        return f"{self.nombre} {self.apellido} {self.telefono} {self.dni}" "Muestra el registro de las tablas"

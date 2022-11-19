from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):
    """Form definition for Producto."""

    class Meta:
        """Meta definition for Productoform."""

        model = Producto
        fields = (
            'proveedores', 
            'tipo',
            'marca', 
            'precio',
            'stock_minimo',
            'stock_actual'

        )
        widgets = {
            'Proveedores': forms.CheckboxSelectMultiple()
        }

# leads/forms.py
from django import forms
from .models import Prospecto

# Formulario Completo (Para Digitalizador)
class ProspectoForm(forms.ModelForm):
    class Meta:
        model = Prospecto
        fields = '__all__'
        exclude = ['fecha_contacto', 'fecha_ingreso']
        widgets = {
            'notas': forms.Textarea(attrs={'rows': 3}),
        }

# Formulario Restringido (Para Vendedor)
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Prospecto
        # El vendedor solo ve estos 3 campos
        fields = ['presupuesto', 'estado', 'notas']
        widgets = {
            'notas': forms.Textarea(attrs={'rows': 3}),
        }
from django import forms
from .models import Plantas, Maceteros, Insumos, Clientes

class PlantasForm(forms.ModelForm):
    class Meta:
        model = Plantas
        fields = ['precio','foto','nombre']

class MaceterosForm(forms.ModelForm):
    class Meta:
        model = Maceteros
        fields = ['precio','foto','nombre','descripcion']

class InsumosForm(forms.ModelForm):
    class Meta:
        model = Insumos
        fields = ['precio','foto','nombre','descripcion']




from django import forms


PRODUCT_TYPE_CHOICES = [
    ('planta','Planta'),
    ('macetero','Macetero'),
    ('insumo','Insumo')
]

class ProductoForm(forms.Form):
    tipo_producto = forms.ChoiceField(choices=PRODUCT_TYPE_CHOICES, label="Tipo de Producto")
    nombre = forms.CharField(max_length=100, label="Nombre")
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripción")
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    foto = forms.ImageField(label="Foto")

    def save(self):
        tipo_producto = self.cleaned_data['tipo_producto']
        nombre = self.cleaned_data['nombre']
        descripcion = self.cleaned_data['descripcion']
        precio = self.cleaned_data['precio']
        foto = self.cleaned_data['foto']

        if tipo_producto == 'planta':
            planta = planta(nombre=nombre, precio=precio, foto=foto)
            planta.save()
        elif tipo_producto == 'macetero':
            macetero = macetero(nombre=nombre, descripcion=descripcion, precio=precio, foto=foto)
            macetero.save()
        elif tipo_producto == 'insumo':
            insumo = insumo(nombre=nombre, descripcion=descripcion, precio=precio, foto=foto)
            insumo.save()
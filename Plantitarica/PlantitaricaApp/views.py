from django.shortcuts import render, redirect
from .forms import ProductoForm

# Create your views here.
def inicio(request):
	context={}
	return render(request,'PlantitaricaApp/inicio.html', context)

def agregar_producto(request):
	context={}
	return render(request,'PlantitaricaApp/agregar_producto.html', context)


def btnAgregarProduc(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pagina_productos')
        else:
            form = ProductoForm()
        return render(request, 'plantitaricaApp/agregar_producto.html', {'form': form})
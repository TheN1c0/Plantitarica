from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Plantas, Maceteros, Insumos, Clientes
# Create your views here.
def inicio(request):
	context={}
	return render(request,'PlantitaricaApp/inicio.html', context)

def agregar_producto(request):
	context={}
	return render(request,'PlantitaricaApp/agregar_producto.html', context)

def Productos(request):
	Planta = Plantas.object.all()
	context={"Plantas":Planta}
	return render(request,'PlantitaricaApp/Productos.html', context)

def PMaceteros(request):
	Macetero = Maceteros.object.all()
	context={"Maceteros":Macetero}
	return render(request,'PlantitaricaApp/Maceteros.html', context)

def PInsumos(request):
	Insumo = Insumos.object.all()
	context={"Insumos":Insumo}
	return render(request,'PlantitaricaApp/Insumos.html', context)


def btnAgregarProduc(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pagina_productos')
        else:
            form = ProductoForm()
        return render(request, 'plantitaricaApp/agregar_producto.html', {'form': form})


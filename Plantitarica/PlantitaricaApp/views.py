from django.shortcuts import render, redirect
from .forms import PlantasForm, MaceterosForm, InsumosForm
from .models import Plantas, Maceteros, Insumos, Clientes
# Create your views here.
def inicio(request):
	context={}
	return render(request,'PlantitaricaApp/inicio.html', context)

def agregar_plantas(request):
	context={}
	return render(request,'PlantitaricaApp/agregar_plantas.html', context)

def agregar_maceteros(request):
	context={}
	return render(request,'PlantitaricaApp/agregar_maceteros.html', context)

def agregar_insumos(request):
	context={}
	return render(request,'PlantitaricaApp/agregar_insumos.html', context)

def Productos(request):
	Planta = Plantas.objects.all()
	context={"Plantas":Planta}
	return render(request,'PlantitaricaApp/Productos.html', context)

def PMaceteros(request):
	maceteros = Maceteros.objects.all()
	context={"Maceteros":maceteros}
	return render(request,'PlantitaricaApp/Maceteros.html', context)

def PInsumos(request):
	Insumo = Insumos.objects.all()
	context={"Insumos":Insumo}
	return render(request,'PlantitaricaApp/Insumos.html', context)

def AcercaDe(request):
	context={}
	return render(request,'PlantitaricaApp/AcercaDe.html', context)

def Contacto(request):
	context={}
	return render(request,'PlantitaricaApp/Contacto.html', context)

def btnAgregarPlantas(request):
    if request.method == 'POST':
        form = PlantasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Productos')
        else:
            form = PlantasForm()
        return render(request, 'plantitaricaApp/agregar_producto.html', {'form': form})

def btnAgregarMaceteros(request):
    if request.method == 'POST':
        form = MaceterosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Productos')
        else:
            form = MaceterosForm()
        return render(request, 'plantitaricaApp/agregar_producto.html', {'form': form})
    
def btnAgregarInsumos(request):
    if request.method == 'POST':
        form = InsumosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Productos')
        else:
            form = InsumosForm()
        return render(request, 'plantitaricaApp/agregar_producto.html', {'form': form})

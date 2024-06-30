from django.shortcuts import render, redirect
from .forms import PlantasForm, MaceterosForm, InsumosForm
from .models import Plantas, Maceteros, Insumos, Clientes, EnCarro
# Create your views here.
def inicio(request):
    v_encarro = EnCarro.objects.all()
    context={"EnCarro": v_encarro}
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
    v_encarro = EnCarro.objects.all()
    context={"Plantas":Planta, "EnCarro": v_encarro}
    return render(request,'PlantitaricaApp/Productos.html', context)

def Base(request):
    v_encarro = EnCarro.objects.all()
    context={"EnCarro": v_encarro}
    return render(request,'PlantitaricaApp/Base.html', context)

def PMaceteros(request):
    maceteros = Maceteros.objects.all()
    v_encarro = EnCarro.objects.all()
    context={"Maceteros":maceteros, "EnCarro": v_encarro}
    return render(request,'PlantitaricaApp/Maceteros.html', context)

def PInsumos(request):
    Insumo = Insumos.objects.all()
    v_encarro = EnCarro.objects.all()
    context={"Insumos":Insumo, "EnCarro": v_encarro}
    return render(request,'PlantitaricaApp/Insumos.html', context)

def AcercaDe(request):
    v_encarro = EnCarro.objects.all()
    context={"EnCarro": v_encarro}
    return render(request,'PlantitaricaApp/AcercaDe.html', context)

def Contacto(request):
    v_encarro = EnCarro.objects.all()
    context={"EnCarro": v_encarro}
    return render(request,'PlantitaricaApp/Contacto.html', context)

def btnAgregarPlantas(request):
    precio = request.POST['precio']
    nombre = request.POST['Nombre']
    foto = request.FILES['foto']
    nuevo_servicio = Plantas(precio=precio, nombre=nombre, foto=foto)
    nuevo_servicio.save()
    return render(request, 'plantitaricaApp/agregar_plantas.html')

def btnAgregarMaceteros(request):
    precio = request.POST['precio']
    nombre = request.POST['Nombre']
    foto = request.FILES['foto']
    nuevo_servicio = Maceteros(precio=precio, nombre=nombre, foto=foto)
    nuevo_servicio.save()
    return render(request, 'plantitaricaApp/agregar_maceteros.html' )
    
def btnAgregarInsumos(request):
    precio = request.POST['iprecio']
    nombre = request.POST['inombre']
    foto = request.FILES['ifoto']
    nuevo_servicio = Insumos(precio=precio, nombre=nombre, foto=foto)
    nuevo_servicio.save()
    return render(request, 'plantitaricaApp/agregar_insumos.html')

def registrarEnCarro(request):
    tipo = request.POST['tipo']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    pagina= request.POST['pagina']
    elemento = EnCarro(tipo= tipo, nombre=nombre, precio=precio)
    elemento.save()

    return redirect(pagina)

def eliminarEncarro(request, nombre):
    producto = EnCarro.objects.filter(nombre=nombre).first()
    pagina_destino = request.POST.get('pagina_destino', 'url_por_defecto')
    if request.method == 'POST':
        producto.delete()
        return redirect(pagina_destino)
    return redirect('lista_productos')
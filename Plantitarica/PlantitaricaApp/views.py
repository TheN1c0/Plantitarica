from django.shortcuts import render, redirect
from .forms import PlantasForm, MaceterosForm, InsumosForm
from .models import Plantas, Maceteros, Insumos, Clientes, EnCarro
# Create your views here.
def inicio(request):
    v_encarro = EnCarro.objects.all()
    total = sum(item.precio * item.cantidad for item in v_encarro)  
    context = {
        "EnCarro": v_encarro,
        "Total": total  
    }
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
    
    total = sum(item.precio * item.cantidad for item in v_encarro)  
    context = {
        "EnCarro": v_encarro,
        "Total": total,
        "Plantas":Planta
    }
    return render(request,'PlantitaricaApp/Productos.html', context)

def Base(request):
    v_encarro = EnCarro.objects.all()
    total = sum(item.precio * item.cantidad for item in v_encarro)  
    context = {
        "EnCarro": v_encarro,
        "Total": total  
    }
    return render(request,'PlantitaricaApp/Base.html', context)

def PMaceteros(request):
    maceteros = Maceteros.objects.all()
    v_encarro = EnCarro.objects.all()
    
    total = sum(item.precio * item.cantidad for item in v_encarro)  
    context = {
        "EnCarro": v_encarro,
        "Total": total,
        "Maceteros":maceteros  
    }
    return render(request,'PlantitaricaApp/Maceteros.html', context)

def PInsumos(request):
    Insumo = Insumos.objects.all()
    v_encarro = EnCarro.objects.all()
 
    total = sum(item.precio * item.cantidad for item in v_encarro)  
    context = {
        "EnCarro": v_encarro,
        "Total": total,
        "Insumos":Insumo 
    }
    return render(request,'PlantitaricaApp/Insumos.html', context)

def AcercaDe(request):
    v_encarro = EnCarro.objects.all()
    total = sum(item.precio * item.cantidad for item in v_encarro)  
    context = {
        "EnCarro": v_encarro,
        "Total": total  
    }
    return render(request,'PlantitaricaApp/AcercaDe.html', context)

def Contacto(request):
    v_encarro = EnCarro.objects.all()
    total = sum(item.precio * item.cantidad for item in v_encarro)  
    context = {
        "EnCarro": v_encarro,
        "Total": total  
    }
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
    nombre_producto = request.POST['nombre']
    precio = request.POST['precio']
    pagina= request.POST['pagina']
    
    verificar_producto = EnCarro.objects.filter(nombre = nombre_producto).exists()
    if verificar_producto:
        producto = EnCarro.objects.get(nombre = nombre_producto)
        producto.cantidad = producto.cantidad + 1
        producto.save()
        
    else:
        elemento = EnCarro(tipo= tipo, nombre=nombre_producto, precio=precio, cantidad = 1)
        elemento.save()

    return redirect(pagina)

def eliminarEncarro(request, nombre):
    producto = EnCarro.objects.filter(nombre=nombre).first()
    pagina_destino = request.POST.get('pagina_destino', 'url_por_defecto')
    if request.method == 'POST' and producto.cantidad == 1:
        producto.delete()
        return redirect(pagina_destino)
    elif producto.cantidad > 1:
        producto.cantidad = producto.cantidad - 1
        producto.save()
        return redirect(pagina_destino)

    return redirect('lista_productos')

from django.shortcuts import get_object_or_404

def actualizar_precio_producto(request, producto_id, nuevo_precio):
    # Obtener el producto por ID
    producto = get_object_or_404(Producto, id=producto_id)

    # Cambiar el valor del precio
    producto.precio = nuevo_precio

    # Guardar los cambios en la base de datos
    producto.save()

    # Redirigir o manejar la respuesta como desees
    return redirect('alguna_url_para_redireccionar')  # Asegúrate de proporcionar una URL válida

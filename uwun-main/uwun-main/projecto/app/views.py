from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def quienessomos(request):
    return render(request, 'app/quienessomos.html')

def verproducto(request):
    return render(request, 'app/verproducto.html')

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/productos.html', data)


def adm(request):
    return render(request, 'app/adm.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def history(request):
    return render(request, 'app/history.html')

def inicioadm(request):
    return render(request, 'app/inicioadm.html')

def iniciosesion(request):
    return render(request, 'app/iniciosesion.html')

def pagar(request):
    return render(request, 'app/pagar.html')

def perfil(request):
    return render(request, 'app/perfil.html')

def publicar(request):
    data ={
        'form': ProductoForm()
    }

    if request.method == 'POST':
        data = {
            'form': ProductoForm()
        }

        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "Producto publicado"
            else:
                data["form"] = formulario
    return render(request, 'app/publicar.html', data)


def register(request):
    return render(request, 'app/register.html')

def subscripcion(request):
    return render(request, 'app/subscripcion.html')

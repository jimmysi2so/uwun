from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def quienessomos(request):
    return render(request, 'app/quienessomos.html')

def verproducto(request):
    return render(request, 'app/verproducto.html')

def productos(request):
    return render(request, 'app/productos.html')

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
    return render(request, 'app/publicar.html')

def register(request):
    return render(request, 'app/register.html')

def subscripcion(request):
    return render(request, 'app/subscripcion.html')

from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def employees(request):
    return render(request, 'calificaciones/index.html')

def crear(request):
    return render(request, 'calificaciones/crear.html')

def editar(request):
    return render(request, 'calificaciones/editar.html')
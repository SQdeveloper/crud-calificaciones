from django.shortcuts import render
from .models import Employees

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def employees(request):
    # employees = Employees.objects.all()    
    from .models import Employees

    employees = Employees.objects.select_related('role').all()

    return render(request, 'calificaciones/index.html', {'employees': employees})

def crear(request):
    return render(request, 'calificaciones/crear.html')

def editar(request):
    return render(request, 'calificaciones/editar.html')
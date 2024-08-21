from django.urls import path
from . import views

urlpatterns = [
    path('', views.employees, name='calificaciones'),        
    path('nosotros', views.nosotros, name='nosotros'),    
    path('calificaciones/crear', views.crear, name='crear'),    
    path('calificaciones/editar', views.editar, name='editar'),    
]

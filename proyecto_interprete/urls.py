from django.contrib import admin
from django.urls import path
from core.views import interprete_view, ejecutar_codigo_ajax 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Ruta principal: Para cargar la página (GET)
    path('', interprete_view, name='interprete_home'),
    
    # 2. Nueva ruta: Para manejar la ejecución AJAX (POST)
    path('ejecutar/', ejecutar_codigo_ajax, name='ejecutar_codigo'), 
]
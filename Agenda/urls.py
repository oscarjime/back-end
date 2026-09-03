from django.contrib import admin
from django.urls import path, include  # Importamos 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
path('', include('nombre_aplicacion.urls')),  # Conecta las rutas de tu app
]

handler404 = 'nombre_aplicacion.views.mi_error_404'
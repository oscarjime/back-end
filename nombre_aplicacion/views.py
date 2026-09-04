from django.shortcuts import render

# Vista para la página principal de bienvenida
def bienvenida(request):
    return render(request, 'bienvenida.html')

# Handler para el error 404 usando plantilla HTML
def mi_error_404(request, exception=None):
    return render(request, '404.html', status=404)
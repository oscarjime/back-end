from django.http import HttpResponse

def bienvenida(request):
    html_contenido = """
    <h1>¡Bienvenido a la aplicación Agenda!</h1>
    <p>Esta es la base técnica de la aplicación desarrollada para la Evaluación 1.</p>
    """
    return HttpResponse(html_contenido)

def mi_error_404(request, exception=None):
    return HttpResponse(
        "<h1>Error 404 - Página no encontrada</h1>"
        "<p>La ruta ingresada no existe en el sistema de la Agenda.</p>",
        status=404
    )
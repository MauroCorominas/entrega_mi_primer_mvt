from django.http import HttpResponse

def saludo(request):
    return HttpResponse('Prueba de conexion')
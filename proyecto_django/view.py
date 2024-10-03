from django.http import HttpResponse

def mi_vista (request):
    return HttpResponse('Hola soy la vista')

def inicio(request):
    return HttpResponse('<h1>Soy la pantalla de inicio</h1>')
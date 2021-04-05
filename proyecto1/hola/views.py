from django.shortcuts import render
from django.http import HttpResponse

# Vista con template
def hola(request):
    return render(request, 'hola/index.html')

#Visatas sin temlplate
def usuarios(request):
    return HttpResponse("Vista de usuarios")

def contabilidad(request):
    return HttpResponse("Contabilidad")

# Parametros sin template
def saludo(request, nombre):
    return HttpResponse(f"Hola {nombre}")

# Parametros con template
def saludoTemplate(request, nombre):
    context = {'name': nombre}
    return render(request, 'hola/saludo.html', context)

# Logica templates
def moneda(request):
    varMoneda = 0
    context = {'money': varMoneda}
    return render(request, 'hola/moneda.html', context)
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def bienvenido(request):
    hola_mundo = "bienvenido"
    return HttpResponse(hola_mundo)


def bienvenido_template(request):
    return render(request, "bienvenido.html")


def bienvenido_dicionario(request):
    mensajes = {"mensaje1": "Valor del mensaje1",
                "mensaje2": "Valor2"}
    return render(request, "bienvenido_dicionario.html", mensajes)


def listar_alumnos(request):
    list_alumnos = [
        {"nombre": "Nombre1", "apellidos":"Apellidos1","dni":"111A"},
        {"nombre": "Nombre2", "apellidos": "Apellidos2", "dni": "111B"},
        {"nombre": "Nombre3", "apellidos": "Apellidos3", "dni": "111C"},
                ]
    contexto = {"listado_alumnos":list_alumnos}
    return render(request, "getion/alumnos.html", contexto)


def adios(request):
    return render(request, "adios.html")

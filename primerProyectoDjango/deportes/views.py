from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def deportes(request):
    deportes = {
                "t_deportes": "DEPORTES",
                "t_futbol": "Futbol",
                "t_basquet": "Basquetbol",
                "d_basquetbol": "es un deporte de equipo, jugado entre dos conjuntos de cinco jugadores cada uno "
                              "durante cuatro períodos o cuartos de diez minutos cada uno.",
                "d_futbol": "deporte de equipo jugado entre dos conjuntos de once jugadores cada uno mientras "
                          "los árbitros se ocupan de que las normas se cumplan correctamente."}
    return render(request, "deportes.html", deportes)


def listar_equipos_mundial(request):
    listado_equipos = [
        {"seleccion": "S1", "continente": "C1", "num_mundiales": "1"},
        {"seleccion": "S2", "continente": "C2", "num_mundiales": "2"},
        {"seleccion": "S3", "continente": "C3", "num_mundiales": "3"},
    ]
    contexto = {"listado_equipos": listado_equipos}
    return render(request, "listar_equipos_mundial.html", contexto)
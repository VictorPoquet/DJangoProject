from django.shortcuts import render
from django.http import HttpResponse


# PAGINA DEPORTES.HTML genera datos base deportes
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


# PAGINA ADD_NEW_EQUIPO_MUNDIAL.HTML envia a la pagina html
def add_new_equipos_mundial(request):
    return render(request, "add_new_equipo_mundial.html")


# Crea los datos base de los equipos, para poder hacer pruebas
def lista_tabla_equipos(request, continente_param, new_equipo):
    listado_equipos = [
        {"seleccion": "S1", "continente": "C1", "num_mundiales": "1"},
        {"seleccion": "S2", "continente": "C2", "num_mundiales": "2"},
        {"seleccion": "S3", "continente": "C3", "num_mundiales": "3"},
    ]
    list_session_equipos = request.session.get("listado_equipos", None)
    if list_session_equipos == None:
        request.session['listado_equipos'] = listado_equipos
        list_session_equipos = listado_equipos

    if not continente_param == None:
        list_session_equipos = list(
            filter(lambda equipo: equipo['continente'] == continente_param, list_session_equipos))
        print("list_session_equipos: ", list_session_equipos)
    if new_equipo:
        list_session_equipos.append(new_equipo)
    return list_session_equipos


# Recoge los datos del post del nuevo equipo
def dicionario_new_equip(request):
    new_seleccion = request.POST['seleccion']
    new_continente = request.POST['continente']
    new_num_mundiales = request.POST['num_mundial']
    new_equip = {"seleccion": new_seleccion, "continente": new_continente, "num_mundiales": new_num_mundiales}
    return new_equip


# PAGINA LISTA_EQUIPOS_MUNDIAL.HTML crea datos base, filtra y recibe los post de los nuevos equipos
def listar_equipos_mundial(request):
    continente_param = None
    new_equipo = []
    titulo_tabla = "Tabla Equipos"

    if request.method == 'POST':
        if request.POST['tipo'] == 'filtrar':
            continente_param = request.POST['continente']
            titulo_tabla = request.POST['titulo_tabla']
        elif request.POST['tipo'] == 'add':
            new_equipo = dicionario_new_equip(request)
    elif request.method == 'GET':
        titulo_tabla = request.GET['titulo_tabla']

    # URL DE LA QUE VENIA
    # last_page =

    listado_equipos = lista_tabla_equipos(request, continente_param, new_equipo)
    contexto = {"listado_equipos": listado_equipos, "titulo": titulo_tabla}

    return render(request, "listar_equipos_mundial.html", contexto)


# PAGINA DE JUGADORES
def jugadores(request):
    return render(request, "jugadores.html")


def add_jugadores(request):
    return render(request, "add_del_jugadores.html")


def del_jugadores(request):
    if request.method == 'POST':
        request
    return render(request, "add_del_jugadores.html")

"""primerProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from clientes.views import add_new_client, delete_client_template, delete_client
from webapp.views import bienvenido, bienvenido_template, bienvenido_dicionario, listar_alumnos, adios
from deportes.views import deportes, listar_equipos_mundial, add_new_equipos_mundial, jugadores, add_jugadores, \
    del_jugadores, actualizar_jugadores

urlpatterns = [
    # APP WEBAPP
    path('admin/', admin.site.urls),
    path('wellcome/', bienvenido),
    path('wellcome_template/', bienvenido_template, name="inicio"),
    path('wellcome_dicionario/', bienvenido_dicionario),
    path('adios/', adios),
    path('alumnos/listar_alumnos', listar_alumnos, name="listado_alumnos"),

    # APP DEPORTES
    path('deportes/', deportes, name="deportes"),
    path('deportes/listar_equipos_mundial', listar_equipos_mundial, name="listar_equipos_deportes"),
    path('deportes/add_new_equipos_mundial', add_new_equipos_mundial, name="add_new_equipos_deportes"),
    path('deportes/jugador', jugadores, name="jugador"),
    path('deportes/jugador/add', add_jugadores, name="jugador-add"),
    path('deportes/jugador/del/<int:id>', del_jugadores, name="jugador-del"),
    path('deportes/jugador/actualizar/<int:id>', actualizar_jugadores, name="jugador-actualizar"),

    # APP CLIENTES COCHES
    # path('clientes', list_client, name="list_clientes"),
    path('clientes/add', add_new_client, name="add_clientes"),
    path('clientes/delete_template', delete_client_template, name="client_del_template"),
    path('clientes/delete/<int:id>', delete_client, name="client_del"),


]

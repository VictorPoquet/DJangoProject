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
from webapp.views import bienvenido, bienvenido_template, bienvenido_dicionario, listar_alumnos, adios
from deportes.views import deportes, listar_equipos_mundial

urlpatterns = [
    #APP WEBAPP
    path('admin/', admin.site.urls),
    path('wellcome/', bienvenido),
    path('wellcome_template/', bienvenido_template, name = "inicio"),
    path('wellcome_dicionario/', bienvenido_dicionario),
    path('adios/', adios),
    path('alumnos/listar_alumnos', listar_alumnos, name="listado_alumnos"),

    #APP DEPORTES
    path('deportes/', deportes, name="deportes"),
    path('deportes/listar_equipos_mundial', listar_equipos_mundial, name="listar_equipos_deportes"),

]

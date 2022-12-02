from django.db import models


# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    equipo = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacionalidad = models.EmailField(max_length=30)
    posicion = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.equipo} {self.edad} {self.nacionalidad} {self.posicion}"

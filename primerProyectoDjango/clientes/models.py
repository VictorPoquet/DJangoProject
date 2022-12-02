from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=60)
    dni = models.CharField(max_length=9)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellidos} {self.dni} {self.email}"


class Coche(models.Model):
    matricula = models.CharField(max_length=7, null=True)
    marca = models.CharField(max_length=40, null=True)
    color = models.CharField(max_length=20, null=False)
    combustible = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Coche: {self.id} {self.matricula} {self.marca} {self.color} {self.combustible}  Cliente: {self.cliente.nombre if self.cliente != None else ''}"


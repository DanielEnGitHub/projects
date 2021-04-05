from django.db import models

# Create your models here.
class Cafeteria(models.Model):
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Empleados(models.Model):
    nombre = models.CharField(max_length=50)
    cafeteria = models.ForeignKey(Cafeteria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    dni = models.IntegerField()
    correo = models.CharField(max_length=150)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    fechaNacimiento = models.DateField(auto_now=True)
    usuario = models.CharField(max_length=60)
    clave = models.CharField(max_length=60)
    foto = models.CharField(max_length=250)
    fotoMiniatura = models.CharField(max_length=250)

    def __str__(self):
        return self.apellido + ", " + self.nombre
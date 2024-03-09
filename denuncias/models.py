from django.db import models

# Create your models here.

"""
@author ngeoffroy
Creo el modelo base de las denuncias
Fields: 
    * id como llave primaria para buscar las denuncias
    * título de la denuncia
    * descripción en caso de querer agregar algún "contexto"
    * imagen de la denuncia a analizar
    * status que representa el estado de la solicitud (0 pendiente, 1 en revisión y 2 terminada)
    * autorizado que representa si la denuncia fué aprobada o no (0 no aprobada, 1 aprobada). Si está aprobada, se sanciona al usuario
    * pena representa el "castigo" que deberá cumplir el usuario
"""

class Denuncia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='denuncias/', width_field=None, height_field=None)
    status = models.PositiveSmallIntegerField(default=0)
    autorizado = models.PositiveSmallIntegerField(default=0)
    pena = models.CharField(max_length=50, default="")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id} {self.titulo}'

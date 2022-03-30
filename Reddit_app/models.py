from distutils.command.upload import upload
import email
from tabnanny import verbose
from django.db import models

class Noticias (models.Model):
    encabezado= models.CharField(max_length=100, blank=False, null=False)
    describcion =models.TextField(blank=False, null=False)
    autor =models.CharField(max_length=100, blank=False, null=False)
    fecha =models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.encabezado


class Comentarios(models.Model):
    nombre= models.CharField(max_length=150, blank=False,null=False)
    email= models.EmailField(max_length=150, blank=False, null=False)
    telefono= models.CharField(max_length=150,blank=False,null=False)
    comentario= models.TextField(blank=False,null=False)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return self.nombre

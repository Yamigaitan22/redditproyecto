from re import search
from django.contrib import admin
from .models import Comentarios, Noticias

# Register your models here.
class NotiAdmin(admin.ModelAdmin):
    list_display =[ "describcion", "autor", "fecha"]
    list_editable=["autor"]
    search_fields= ["describcion", "autor"]
    list_filter=["fecha"]
    list_per_page=10

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ["nombre","email","telefono","comentario"]
    list_editable = ["comentario"]
    search_fields = ["email"]
    list_per_page = 10 



admin.site.register(Noticias,NotiAdmin )
admin.site.register(Comentarios)

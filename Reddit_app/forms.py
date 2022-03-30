from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import Comentarios


class ComentariosForm(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = ["nombre", "email", "telefono", "comentario"]
        #fields = '__all__'
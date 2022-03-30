from ast import If
from urllib import request
from django.shortcuts import render
from .models import  Noticias
from .forms import ComentariosForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about-us.html')

def services(request):
    return render(request, 'app/services.html')

def typography(request):
    return render(request, 'app/typography.html')

def tabsaccordions(request):
    return render(request, 'app/tabs-and-accordions.html')

def news(request):
    noticia= Noticias.objects.all()

   
    datos = {
       "Noticias" : noticia,
      
    }
    return render(request, 'app/news.html', datos)

def contact(request):
    datos = {
        'form': ComentariosForm
    }
    if request.method == 'POST':
        formulario = ComentariosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos['form'] = formulario

    return render(request, 'app/contact-us.html', datos)

def newspost(request):
    return render(request, 'app/news-post.html')

def single(request):
    return render(request, 'app/single-services.html')

def Terminos(request):
    return render(request, 'app/terms-and-conditions.html')


def Privacidad(request):
    return render(request, 'app/privacy-policy.html')

def Busqueda(request):
    if request.GET['Busqueda']:
        query=request.GET['Busqueda']
        noticias= Noticias.objects.filter(encabezado__icontains=query)
        datos={
            "result": noticias,
            "query" : query
        }
        return  render (request, 'app/busqueda.html', datos)
    else:
        return render (request, 'app/busqueda.html')

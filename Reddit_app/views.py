from django.shortcuts import render, redirect
from .models import  Noticias, Comentarios
from .forms import ComentariosForm, userForm, loginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
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


def reddit1(request):
    return render(request, 'app/reddit1.html')

def reddit2(request):
    return render(request, 'app/reddit2.html')

def reddit3(request):
    return render(request, 'app/reddit3.html')

def reddit4(request):
    return render(request, 'app/reddit4.html')

def reddit5(request):
    return render(request, 'app/reddit5.html')

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


        

class Registro(View):
    form_class = userForm
    initial = {'key': 'value'}
    template_name = 'app/registro.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        return super (Registro, self).dispatch(request, *args, **kwargs)

class CustomLoginView(LoginView):
    form_class = loginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)

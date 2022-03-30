from django.urls import path, include
from .views import Busqueda, about, index, about, services, typography, tabsaccordions, news, contact, newspost, single, Terminos,Privacidad,Busqueda
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', index, name='Inicio'),
    path('about/', about, name='Sobre Nosotros'),
    path('services/', services, name='Servicios'),
    path('typography/', typography, name='Tipografia'),
    path('tabsaccordions/', tabsaccordions, name='Pestañas y Acordes'),
    path('news/', news, name='Noticias'),
    path('contact-us/', contact, name='Contactanos'),
    path('news-post/', newspost, name='Noticias Publicadas'),
    path('single-services/', single, name='Soluciones'),
    path('terms-conditions/', Terminos, name='Terminos'),
    path('privacy-policy/', Privacidad, name='Privacidad'),
    path('buscar/', Busqueda, name='buscar'),
    
]
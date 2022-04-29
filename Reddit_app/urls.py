from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import Busqueda,about, index, about, reddit1, reddit2, reddit3, reddit4, reddit5, services, typography, tabsaccordions, news, contact, newspost, single, Terminos,Privacidad,Busqueda, Registro, CustomLoginView
from django.conf import settings
from .forms import loginForm
from django.contrib.auth import views as auth_views

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
    path('vistas/', reddit1, name='Vistas'),
    path('comentarios/', reddit2, name='Comentarios'),
    path('descargas/', reddit3, name='imagenes'),
    path('votos/', reddit4, name='Votos'),
    path('reacciones/', reddit5, name='reacciones'),
    path('terms-conditions/', Terminos, name='Terminos'),
    path('privacy-policy/', Privacidad, name='Privacidad'),
    path('buscar/', Busqueda, name='buscar'),
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='app/login.html',authentication_form=loginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
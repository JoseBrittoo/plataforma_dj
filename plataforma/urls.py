
from django.contrib import admin
from django.urls import path
from app_plataforma.views import home, cadusuario, usuario, flogin, dlogin, paginaInicial, logouts, alterarSenha
#from app_plataforma import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('cadusuario/', cadusuario, name='cadusuario'),
    path('usuario/', usuario), 
    path('flogin/', flogin, name = 'flogin'),
    path('dlogin/', dlogin, name = 'dlogin'),
    path('paginaInicial/', paginaInicial),
    path('logouts/', logouts, name = 'logouts'),
    path('alterarSenha/', alterarSenha, name = 'alterarSenha')
]

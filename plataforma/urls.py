
from django.contrib import admin
from django.urls import path
from app_plataforma.views import home, cadusuario, usuario, flogin, dlogin, paginaInicial, logouts, alterarSenha, pgInical_proprietario, pgInicial_aluno, pgInicial_afiliado

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
    path('alterarSenha/', alterarSenha, name = 'alterarSenha'),
    path('pgInical_proprietario/', pgInicial_proprietario name='pgInical_proprietario'),
    path('pgInicial_aluno/', pgInicial_aluno, name='pgInicial_aluno'),
    path('pgInicial_afiliado/', pgInicial_afiliado, name='pgInicial_afiliado')
]

from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from app_plataforma.views import home, cadusuario, usuario, flogin, dlogin, paginaInicial, logouts, alterarSenha, cadcurso, catalogocurso, detalhescurso
from app_plataforma.views import CustomPasswordResetConfirmView

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
    path('cadcurso/', cadcurso, name = 'cadcurso'),
    path('catalogocurso/', catalogocurso, name='catalogocurso'),
    path('curso/<int:curso_id>/', detalhescurso, name='detalhescurso'),
   

    #para recuperação de senha
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="recuperar_senha/recuperar_senha.html"), name="reset_password"),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name="recuperar_senha/redefinicao_enviada.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(template_name="recuperar_senha/nova_senha.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="recuperar_senha/redefinicao_comp.html"), name="password_reset_complete"),
]
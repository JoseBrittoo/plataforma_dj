from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Curso, Modulo
from .forms import CursoForm, ModuloFormSet
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

#Formulário de cadastro de usuários
def cadusuario(request):
    return render(request,'cadusuario.html')


#Inserção dos dados dos usuários no banco
def usuario(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'cadusuario.html',data)

#Formulário de cadastro de login
def flogin(request):
    return render(request, 'flogin.html')

#Processar o login
def dlogin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/paginaInicial/')
    else:
        data['msg'] = 'Senha ou usuario incorreto!'
        data['class'] = 'alert-danger'
        return render(request, 'flogin.html', data)


#Página inical do sistema
def paginaInicial(request):
    return render(request, 'paginaInicial/pgInicial.html')

#Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/')

#Alterar senha
def alterarSenha(request):
    data = {}
    if request.method == 'POST':
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        
        if new_password1 == new_password2:
            user = User.objects.get(email=request.user.email)
            
            if user.check_password(new_password1):
                data['msg'] = 'A nova senha não pode ser igual à senha anterior.'
                data['class'] = 'alert-danger'
            else:
                user.set_password(new_password1)
                user.save()
                logout(request)
                return redirect('/flogin/')
        else:
            data['msg'] = 'Senhas não coincidem!'
            data['class'] = 'alert-danger'
            
        return render(request, 'alterarSenha.html', data)
            
    return render(request, 'alterarSenha.html')

#Cadastrar curso
def cadcurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        formset_modulos = ModuloFormSet(request.POST, prefix='modulos')

        if form.is_valid() and formset_modulos.is_valid():
            # Salvar o curso principal
            curso = form.save()

            # Salvar os módulos associados ao curso principal
            for form_modulo in formset_modulos:
                if form_modulo.cleaned_data:
                    modulo = form_modulo.save(commit=False)
                    modulo.curso = curso
                    modulo.save()

            messages.success(request, 'Curso cadastrado com sucesso!')
            return redirect('catalogocurso')  # Redirecionar para uma página de sucesso
        else:
            messages.error(request, 'Formulário inválido!')      
    else:
        form = CursoForm()
        formset_modulos = ModuloFormSet(prefix='modulos')

    return render(request, 'cadcurso.html', {
        'form': form,
        'formset_modulos': formset_modulos,
    })

#Sobre o catalogo de cursos
def catalogocurso(request):
    cursos = Curso.objects.all()
    return render(request, 'catalogocurso.html', {'cursos': cursos})

#Detalhes dos cursos
def detalhescurso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'detalhescurso.html', {'curso': curso})

from django.contrib.auth.views import PasswordResetConfirmView

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'recuperar_senha/nova_senha.html'  # Caminho para o seu template personalizado

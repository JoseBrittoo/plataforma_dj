from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        user_type = request.POST['user-type']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            if user_type == 'proprietario':
                return redirect('pgInical_proprietario')
            elif user_type == 'aluno':
                return redirect('pgInicial_aluno')
            elif user_type == 'afiliado':
                return redirect('pgInicial_afiliado')
        else:
            msg = 'Senha ou usuário incorretos!'
            return render(request, 'flogin.html', {'msg': msg, 'class': 'alert-danger'})

    return render(request, 'flogin.html')

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
    
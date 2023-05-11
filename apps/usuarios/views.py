from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages


def cadastro(request, template_name='usuarios/cadastro.html'):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():

            nome=form['nome_login'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.info(request, 'Usuário já cadastrado')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso')
            return redirect('login')

    return render(request, template_name, {'form': form})


def login(request, template_name='usuarios/login.html'):

    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()

            usuario = auth.authenticate(request, username=nome, password=senha)
            if not usuario:
                messages.error(request, 'Erro ao efetuar login')
                return redirect('login')

            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso')
            return redirect('index')

    return render(request, template_name, {"form": form})


def logout(request):
    auth.logout(request)
    messages.info(request, 'Logout efetuado com sucesso!')
    return redirect('login')
from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

def login(request, template_name='usuarios/login.html'):
    form = LoginForms()
    return render(request, template_name, {"form": form})

def cadastro(request, template_name='usuarios/cadastro.html'):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                return redirect ('cadastro')

            nome=form['nome_login'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})
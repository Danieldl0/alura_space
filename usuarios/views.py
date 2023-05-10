from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

def login(request, template_name='usuarios/login.html'):
    form = LoginForms()
    return render(request, template_name, {"form": form})

def cadastro(request, template_name='usuarios/cadastro.html'):
    form = CadastroForms()
    return render(request, template_name, {"form": form})
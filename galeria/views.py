from django.shortcuts import render
from django.http import HttpResponse

def index(request, template_name="galeria/index.html"):
    return render(request, template_name)

def imagem(request, template_name="galeria/imagem.html"):
    return render(request, template_name)
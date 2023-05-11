from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Fotografia
from django.contrib import messages

#view da lista de todas as fotografias
def index(request, template_name="galeria/index.html"):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')

    #filtrando e ordenando as fotografias pela data e se está habilitado a opção publicada.
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, template_name, {"cards":fotografias})

#view fotografia pelo id
def imagem(request, id ,template_name="galeria/imagem.html"):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        redirect('login')

    fotografia = get_object_or_404(Fotografia, pk=id)
    return render(request, template_name, {"fotografia": fotografia})

#view de busca
def buscar(request, template_name="galeria/buscar.html"):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_busca = request.GET["buscar"]
        if nome_a_busca:
            fotografias = fotografias.filter(nome__icontains = nome_a_busca)

    return render(request, template_name, {"cards":fotografias})
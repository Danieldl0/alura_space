from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Fotografia

#view da lista de todas as fotografias
def index(request, template_name="galeria/index.html"):
    #filtrando e ordenando as fotografias pela data e se está habilitado a opção publicada.
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, template_name, {"cards":fotografias})

#view fotografia pelo id
def imagem(request, id ,template_name="galeria/imagem.html"):
    fotografia = get_object_or_404(Fotografia, pk=id)
    return render(request, template_name, {"fotografia": fotografia})

#view de busca
def buscar(request, template_name="galeria/buscar.html"):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_busca = request.GET["buscar"]
        if nome_a_busca:
            fotografias = fotografias.filter(nome__icontains = nome_a_busca)

    return render(request, template_name, {"cards":fotografias})
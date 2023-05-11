from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForm

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
def buscar(request, template_name="galeria/index.html"):


    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_busca = request.GET["buscar"]
        if nome_a_busca:
            fotografias = fotografias.filter(nome__icontains = nome_a_busca)

    return render(request, template_name, {"cards":fotografias})

#view de criação de nova imagem
def nova_imagem(request, template_name="galeria/nova_imagem.html"):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')

    form = FotografiaForm()

    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES)
        if form.is_valid():
            fotografia = form.save(commit=False)
            fotografia.usuario = request.user
            fotografia.save()
            messages.success(request, f'{fotografia.nome} cadastrada com sucesso')
            return redirect('nova_imagem')

    return render(request, template_name, {'form': form})


def editar_imagem(request, id, template_name="galeria/editar_imagem.html"):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')

    fotografia = get_object_or_404(Fotografia, pk=id)
    form = FotografiaForm(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto editada com sucesso')
            return redirect('index')


    return render(request, template_name, {'form': form, "id":id})


def deletar_imagem(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')

    fotografia = get_object_or_404(Fotografia, pk = id)
    fotografia.delete()
    messages.success(request, 'Deletado com sucesso')
    return redirect('index')


def filtro(request, categoria, template_name='galeria/index.html'):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True,categoria=categoria)

    return render(request, template_name, {"cards": fotografias})
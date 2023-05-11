from django.urls import path
from apps.galeria.views import index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem, filtro

urlpatterns = [
    path('', index, name="index"),
    path('imagem/<int:id>', imagem, name="imagem"),
    path('buscar/', buscar, name="buscar"),
    path('nova_imagem/', nova_imagem, name="nova_imagem"),
    path('editar_imagem/<int:id>', editar_imagem, name="editar_imagem"),
    path('deletar_imagem/<int:id>', deletar_imagem, name="deletar_imagem"),
    path('filtro/<str:categoria>', filtro, name="filtro"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial que lista os itens do menu
    path('add/', views.add_item, name='add_item'),  # Página para adicionar um novo prato
    path('update/<int:id>/', views.update_item, name='update_item'),  # Página para editar um prato
    path('delete/<int:id>/', views.delete_item, name='delete_item'),  # Rota para deletar um prato
]

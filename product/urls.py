from django.urls import path
from . import views

urlpatterns=[
    # Rota para lista de produtos
    path("", views.product_list, name="product_list"),
    # Rota para adicionar produtos
    path("add/", views.product_create, name="product_create"),

    # Rota para editar um produto específico
    path("edit/<int:pk>", views.product_update, name="product_update"),

    # Rota para deletar um produto
    path("delete/<int:pk>/", views.product_delete, name="product_delete"),
]
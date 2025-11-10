from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProductForm
from .models import Produto

# Create your views here.

# view da tela inicial, listar todos os produtos
def product_list(request):
    # Busca todos os objetos Produto no banco de dados
    produtos = Produto.objects.all()
    # Renderiza o template, passando os produtos como contexto
    return render(request, "product_list.html", {"produtos": produtos})

# view para criar um produto
def product_create(request):
    if request.method == "POST":
        # Se o método for POST, o formulário foi enviado
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Salva o novo produto no banco de dados
            messages.success(request, "Produto criado com sucesso!")
            return redirect("product_list")  # Redireciona para a lista de produtos
    else:
        # Se o método for GET, exibe um formulário em branco
        form = ProductForm()

    # Renderiza o template do formulário, passando o form como contexto
    return render(request, "product_form.html", {"form": form})

# view para atualizar um produto
def product_update(request, pk):
    # Busca o produto pela chave primária (pk) ou retorna um erro 404 se não encontrar
    produto = get_object_or_404(Produto, pk=pk)   

    if request.method == "POST":
        # Passamos 'instance=produto' para que o formulário saiba que estamos editando um objeto existente
        form = ProductForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect("product_list")
    else:
        # Ao carregar a página (GET), o formulário é preenchido com os dados do produto
        form = ProductForm(instance=produto)

    # Reutiliza o mesmo template do formulário de criação
    return render(request, "product_form.html", {"form": form, "produto": produto})

# view para deletar um produto
def product_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == "POST":
        # Se o formulário de confirmação for enviado (POST), deleta o objeto
        produto.delete()
        return redirect("product_list")

    # Se for um acesso via GET, exibe a página de confirmação
    return render(request, "product_confirm_delete.html", {"produto": produto})
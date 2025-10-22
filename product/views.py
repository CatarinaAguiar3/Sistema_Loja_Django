from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProductForm 

# Create your views here.
# View da tela inicial (listar todos os produtos)
def product_list(request):
    # Busca todos os objetos (Produtos) no banco de dados
    produtos = Produto.objects.all()
    #Renderiza o template, passando os produtos como contexto
    return render(request, "product_list.html", {"produtos":produtos})

# View para criar um produto
def product_create(request):
    if request.method == "POST":
        # Se o método for POST, o formulário será enviado
        form = ProductForm(request.POST) # formulário para requisição de "POST"
        if form.is_valid(): # Se o formulário for válido
            form.save() # Salvar o novo produto no banco de dados
            return redirect("product_list") #Redirecionar para a lista de produtos (tela inicial)
    else:
        # Se o método for GET, será exibido um formulário em branco
        form = ProductForm()
    # Renderizar o template do formulário, passando o "form" como contexto
    return render(request, "product_form.html", {"form":form})    

# View para atualizar um produto
def product_update(request, pk):
    # Busca o produto pela chave primária (pk) ou retorna um erro 404 se não enco
    produto = get_object_or_404(Produto, pk=pk)

    # Será passado 'instance=produto' para que o formulário saiba que estamos edi 
    form = ProductForm(request.POST, instance=produto)
    if form.is_valid():
        form.save()
        return redirect("product_list") # Retorna para a página inicial
    else:
        # Ao carregar a página (GET), o formulário é preenchido com os dados do produto
        form = ProductForm(instance=produto)

    # Reutilizar o mesmo template do formulário de criação
    return render(request, "product_form.html", {"form":form}) 

# View para deletar um produto
def product_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == "POST":
        # Se o formulário de confirmação for enviado (POST), deleta o objeto
        produto.delete() # Equivale ao "DROP" do SQL
        return redirect("product_list")
    # Se for um acesso via GET, exibe a página de confirmação
    return render(request, "product_confirm_delete.html", {"produto": produto})
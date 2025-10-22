from django.db import models

# Create your models here.
class Produto(models.Model):
    nome=models.CharField(max_length=100, null=False) # Campo com no máximo 100 caracteres
    descricao=models.TextField(null=False) # Campo do tipo "Text" que cabe um texto muito grande (com vários caracteres)
    preco=models.DecimalField(max_digits=10, decimal_places=2,null=False) # Campo do tipo "decimnal", com até 10 dígitos e com 2 casas decimais
    quantidade=models.PositiveIntegerField(null=False) # Campo inteiro e positivo. Pois, "Quantidade" não pode ser negativa ou 0 e também deve ser um valor inteiro.
    url_imagem=models.URLField(max_length=500, blank=True, null=False) # Campo próprio para URL, com comprimento de no máximo 500 caracteres
    # blank = True -> Opção para abrir a página em nova guia
    # null = False -> Não pode ser nula

    def __str__(self):
        return self.nome
    
# class Clientes(models.Model):
#     nome=models.CharField(max_lenght=100)
#     email=models.EmailField(unique=True)
#     telefone= models.CharField(max_lenght=15, blank=True, null=True)

#     def __str__(self):
#         return self.nome    
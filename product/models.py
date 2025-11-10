from django.db import models
import uuid
import os
from hashlib import md5

# Create your models here.
def gerar_nome_unico_imagem(instance, filename):
    """Gera um nome único para a imagem usando UUID e hash MD5"""
    # Obtém a extensão do arquivo original
    ext = filename.split(".")[-1]
    # Gera um UUID único
    uuid_id = str(uuid.uuid4())
    # Cria um hash MD5 do nome original + UUID para evitar colisões
    hash_nome = md5(f"{filename}{uuid_id}".encode()).hexdigest()
    # Retorna o caminho completo com o novo nome
    return os.path.join("imagens-produtos", f"{hash_nome}.{ext}")
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    
    imagem = models.ImageField(upload_to="produtos/", blank=True, null=True)
    url_imagem = models.URLField(blank=True, null=True)  # Manter para compatibilidade
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
    @property
    def imagem_url(self):
        """Retorna a URL da imagem, priorizando upload sobre URL externa"""
        if self.imagem:
            return self.imagem.url
        return self.url_imagem
    
# class Clientes(models.Model):
#     nome=models.CharField(max_lenght=100)
#     email=models.EmailField(unique=True)
#     telefone= models.CharField(max_lenght=15, blank=True, null=True)

#     def __str__(self):
#         return self.nome    
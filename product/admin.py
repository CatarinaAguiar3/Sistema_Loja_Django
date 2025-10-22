from django.contrib import admin

# Register your models here.
# Importar da pasta "models" a classe "Produto"
from .models import Produto

# Registra o modelo Produto par que ele apareça na interface da administração
admin.site.register(Produto)
from django import forms
from .models import Produto

class ProductForm(forms.ModelForm):
    class Meta:
        model= Produto
        # Definir quais campos do modelo serão exibidos no formulário
        fields = ["nome", "descricao", "preco", "quantidade", "url_imagem"]
        # Customizar os widgets (é opcional)
        widgets={
            "nome":forms.TextInput(attrs={"class":"form-control"}),
            "descricao": forms.Textarea(attrs={"class":"form-control", "rows": 3}),
            "preco": forms.NumberInput(attrs={"class":"form-control"}),
            "quantidade":forms.NumberInput(attrs={"class":"form-control"}),
            "url_imagem": forms.URLInput(attrs={"class":"form-control"})
        } 
from django import forms
from .models import Produto

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produto
        # Define quais campos do modelo serão exibidos no formulário
        fields = ["nome", "descricao", "preco", "quantidade", "imagem", "url_imagem"]
        # (Opcional) Você pode customizar os widgets se quiser
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "preco": forms.NumberInput(attrs={"class": "form-control"}),
            "quantidade": forms.NumberInput(attrs={"class": "form-control"}),
            "imagem": forms.FileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
            "url_imagem": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ou insira uma URL da imagem",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["imagem"].help_text = "Faça upload de uma imagem do produto"
        self.fields["url_imagem"].help_text = "Ou cole o link de uma imagem externa"
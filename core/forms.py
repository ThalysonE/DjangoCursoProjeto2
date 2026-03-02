from django import forms
from .models import Produto

class ContatoForms(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label= "Email", max_length=100)
    assunto = forms.CharField(label="Assunto", max_length=120)
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea())

class ProdutoModelForms(forms.ModelForm):
    class Meta:
        model = Produto #informa qual model ele vai utilizar
        fields = ['nome', 'preco', 'estoque', 'imagem']
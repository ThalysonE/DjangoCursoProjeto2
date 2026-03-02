from django.db import models
from stdimage.models import StdImageField


# SIGNALS
from django.db.models import signals, SlugField  # para realizar uma ação antes ou depois do envio do formulario
from django.template.defaultfilters import slugify #cria uma slugy para os  nomes dos produtos(um texto valido para ficar na url)


class Base(models.Model):
    criado = models.DateField("Criação", auto_now_add=True)
    modificacao = models.DateField("Modificação", auto_now=True)
    ativo = models.BooleanField("Ativo?", default=True)

class Produto(Base):
    nome = models.CharField("Nome", max_length=180)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField("Estoque")
    imagem = StdImageField('Image', upload_to='produtos', variations={"thumb": (124,124)})
    slug = SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def produto_pre_save(signal, instance, sender,**kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)

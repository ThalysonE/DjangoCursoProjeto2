from django.shortcuts import render
from .forms import ContatoForms
from django.contrib import messages
def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForms(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            assunto = form.cleaned_data["assunto"]
            mensagem = form.cleaned_data["mensagem"]

            print("Mensage enviada")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"Assunto: {assunto}")
            print(f"Mensagem: {mensagem}")

            messages.success(request, "Enviado com Sucesso!")
            form = ContatoForms()
        else:
            messages.error(request, "Erro ao enviar dados do formulário")
    context = {
        "form": form
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')


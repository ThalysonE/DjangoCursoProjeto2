from django.shortcuts import render
from .forms import ContatoForms
from django.contrib import messages

#importacoes para enviar email
import smtplib
from email.message import  EmailMessage
def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForms(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            remetente = "thalysonelione80@gmail.com"
            senha = "snfs qmsn rxkg rnvq" #senha do app do google

            #Pegando todos os dados do formulario
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            assunto = form.cleaned_data["assunto"]
            mensagem = form.cleaned_data["mensagem"]

            #Criando o email
            msg = EmailMessage()
            msg["From"] = remetente
            msg["To"] = email
            msg["Subject"] = assunto
            msg.set_content(mensagem)

            #enviando o email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email:
                email.login(remetente,senha)
                email.send_message(msg)
            """
                nome = form.cleaned_data["nome"]
                email = form.cleaned_data["email"]
                assunto = form.cleaned_data["assunto"]
                mensagem = form.cleaned_data["mensagem"]
    
                print("Mensage enviada")
                print(f"Nome: {nome}")
                print(f"Email: {email}")
                print(f"Assunto: {assunto}")
                print(f"Mensagem: {mensagem}")
            """
            messages.success(request, "Email enviado com Sucesso!")
            form = ContatoForms()
        else:
            messages.error(request, "Erro ao enviar o Email")
    context = {
        "form": form
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')


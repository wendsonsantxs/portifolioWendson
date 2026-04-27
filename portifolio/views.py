from django.shortcuts import render

from core.models import Pessoal
from portifolio.models import Certificado, Projeto


def home(request):
    perfil = Pessoal.objects.first()
    pessoal = Pessoal.objects.first()
    lista_certificados = Certificado.objects.all()

    contexto = {
        'perfil': perfil,
        'pessoal': pessoal,
        'certificados': lista_certificados
    }
    return render(request, 'portifolio/home.html', contexto)



def projetos(request):
    lista_projetos = Projeto.objects.all()

    contexto = {
        'projetos': lista_projetos
    }
    return render(request, 'portifolio/projetos.html', contexto)


def contato(request):
    pessoal = Pessoal.objects.first()

    return render(request, 'portifolio/contato.html', {'pessoal': pessoal})
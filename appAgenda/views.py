from django.shortcuts import render
from .models import *

# Create your views here.

def getTipoPessoa():
    user = Usuario.objects.all()

    pessoal = []
    institucional = []

    for cadastros in user:
        if cadastros.tipo_pessoa == "Instituição":
           institucional.append(cadastros.nome)
           return cadastros.nome

        else:
            pessoal.append(cadastros.nome)
            return cadastros.nome





def CriarUsuario(request):

    return render(request, 'cadastro.html', context=None)
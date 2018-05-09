from django.db import models

# Create your models here.
class TipoPessoa(models.Model):
    instituicao = 'instituição'
    pessoal = 'pessoal'

    TIPO_PESSOA_CHOICES = (
        ('instituicao','Instituição'),
        ('pessoal','Pessoal')
    )

    tipo_pessoa = models.CharField(max_length=12, choices=TIPO_PESSOA_CHOICES, default=pessoal)

    def __str__(self):
        return self.tipo_pessoa

class Usuario(TipoPessoa):
    nome = models.CharField('Nome', max_length=50, blank=False, null=False)
    user_name = models.CharField('Nome do perfil', max_length=50, blank=False, null=False)
    senha = models.CharField('Senha', max_length=20, blank=False, null=False)
    email = models.EmailField('Email', max_length=50, blank=False, null=False)
    telefone = models.CharField('Telefone', max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nome


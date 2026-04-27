from django.db import models

# Create your models here.
from django.db import models

class Pessoal(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    descricao_contato = models.TextField()
    curso = models.CharField(max_length=100)
    periodo = models.IntegerField()
    email = models.EmailField()
    git = models.URLField()
    linked = models.URLField()
    url_imagem = models.URLField()


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Informações Pessoais"
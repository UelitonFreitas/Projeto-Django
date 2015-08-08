from django.db import models
from django.utils import timezone


class Pergunta(models.Model):
    pergunta = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.pergunta

    def foi_publicado_recentemente(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1)

class Escolha(models.Model):
    pergunta = models.ForeignKey(Pergunta)
    escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.escolha

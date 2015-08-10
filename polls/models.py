from django.db import models
from django.utils import timezone


class Pergunta(models.Model):
    pergunta = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.pergunta

    def foi_publicado_recentemente(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1)

    foi_publicado_recentemente.admin_order_field = 'pub_date'
    foi_publicado_recentemente.boolean = True
    foi_publicado_recentemente.short_description = 'Foi publicado recentemente?'

class Escolha(models.Model):
    pergunta = models.ForeignKey(Pergunta)
    escolha = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.escolha

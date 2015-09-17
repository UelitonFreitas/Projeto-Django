from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Pergunta

class TestesDosMetodosDeUmaPergunta(TestCase):

    def testa_se_pergunta_foi_publicada_recentemente_para_uma_pergunta_futura(self):
        """
        O metodo foi_publicada_recentemente deve retornar Falso para perguntas com data de publicacao
        futuras
        """
        mes_que_vem = timezone.now() + datetime.timedelta(days=30)
        pergunta_futura = Pergunta(pub_date=mes_que_vem)
        self.assertEqual(pergunta_futura.foi_publicado_recentemente(), False)

    def testa_se_pergunta_foi_publicada_recentemente_para_uma_pergunta_antiga(self):
        """
        O metodo foi publicado recentemente deve retornar Falso para uma pergunta criada a mais
        de um dia.
        """

        mes_passado = timezone.now() - timezone.timedelta(days=30)
        pergunta_antiga = Pergunta(pub_date = mes_passado)

        self.assertEqual(pergunta_antiga.foi_publicado_recentemente(), False)

    def testa_se_pergunta_foi_publicada_recentemente_para_uma_pergunta_publicada_recentemente(self):
        """
        O metodo foi publicado recentemente deve retornar True para uma pergunta criada a exatamente
        um dia atras.
        """
        ontem = timezone.now() - timezone.timedelta(days=1)
        pergunta_recente = Pergunta(pub_date=ontem)

        self.assertEqual(pergunta_recente.foi_publicado_recentemente(), True)

def cria_pergunta(texto, dias):
    """
    Creates a question with the given `question_text` published the given
    number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    tempo = timezone.now() + datetime.timedelta(days=dias)
    return Pergunta.objects.create(pergunta=texto,
                                   pub_date=tempo)

class TestaViewDaPergunta(TestCase):

    def testa_index_sem_perguntas(self):
        """
        Se nao existe pergunta, uma menssagem deve ser mostrada
        """

        respotas = self.client.get(reverse('polls:index'))

        self.assertEqual(respotas.status_code, 200)
        self.assertContains(respotas, "Nao ha perguntas")
        self.assertQuerysetEqual(respotas.context['lista_das_ultimas_perguntas'], [])

    def testa_index_com_uma_pergunta_passada(self):
        """
        Perguntas com datas de publicao passadas devem ser mostradas na view
        """

        cria_pergunta(texto="Pergunta passada.", dias=-30)

        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['lista_das_ultimas_perguntas'],
            ['<Pergunta: Pergunta passada.>']
        )

    def testa_index_com_uma_pergunta_futura(self):
        """
        Uma pergunta com data futura nao deve ser mostraa na view.
        """
        cria_pergunta(texto="Pergunta futura.", dias=30)
        resposta = self.client.get(reverse('polls:index'))
        self.assertContains(resposta, "Nao ha perguntas",
                            status_code=200)
        self.assertQuerysetEqual(resposta.context['lista_das_ultimas_perguntas'], [])

    def testa_index_com_pergunta_futura_e_passada(self):
        """
        Mesmo se uma pergunta existir, apenas perguntas passadas devem ser mostradas.
        """

        cria_pergunta(texto="Pergunta Passada", dias=-30)
        cria_pergunta(texto="Pergunta Futura", dias=30)

        resposta = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            resposta.context['lista_das_ultimas_perguntas'],
            ['<Pergunta: Pergunta Passada>']
        )


    def testa_index_com_duas_perguntas_passadas(self):
        """
        A index das perguntas deve retornar multiplas perguntas.
        """

        cria_pergunta(texto="Pergunta passada 1", dias=-30)
        cria_pergunta(texto="Pergunta passada 2", dias=-5)

        resposta = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            resposta.context['lista_das_ultimas_perguntas'],
            ['<Pergunta: Pergunta passada 2>', '<Pergunta: Pergunta passada 1>']
        )

    def testa_view_de_detalhe_de_uma_pergunta_com_data_futura(self):
        """
        O detalhamento de uma pergunta com data futura deve retornar o erro 404
        """

        pergunta_futura = cria_pergunta(texto="Pergunta futura", dias=30)
        resposta = self.client.get(reverse('polls:detalhe', args=(pergunta_futura.id,)))
        self.assertEqual(resposta.status_code, 404)

    def testa_view_de_detalhe_com_uma_pergunta_passdata(self):
        """
        O detahe de uma pergunta com data de publicacao passada dever ser mostrada.
        """

        pergunta_passada = cria_pergunta(texto="Pergunta passda", dias=-5)

        resposta = self.client.get(reverse('polls:detalhe', args=(pergunta_passada.id,)))

        self.assertContains(resposta, pergunta_passada.pergunta, status_code=200)


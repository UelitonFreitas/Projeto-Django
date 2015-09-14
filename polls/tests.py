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

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        cria_pergunta(texto="Pergunta passada.", dias=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['lista_das_ultimas_perguntas'],
            ['<Pergunta: Pergunta passada.>']
        )

    '''def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.",
                            status_code=200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
    '''
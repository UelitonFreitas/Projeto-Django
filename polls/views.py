from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader, RequestContext
from polls.models import Pergunta


def busca_tadas_as_perguntas_ordenadas_por_data():
    return Pergunta.objects.order_by('-pub_date')[:5]


def index(request):

    lista_das_ultimas_perguntas = busca_tadas_as_perguntas_ordenadas_por_data()

    contexto = {'lista_das_ultimas_perguntas': lista_das_ultimas_perguntas}

    #saida = ', '.join([p.pergunta_texto for p in lista_das_ultimas_perguntas])

    return render(request, 'polls/index.html', contexto)

def detalhes(request, pergunta_id):

    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    return render(request, 'polls/detalhe.html', {'pergunta': pergunta})

def resultados(request, pergunta_id):
    resposta = "Voce esta procurando resultados da pergunda %s."
    return HttpResponse(resposta % pergunta_id)

def voto(request, pergunta_id):
    return HttpResponse("voce esta votando da pergunta %s." % pergunta_id)
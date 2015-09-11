from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from polls.models import Pergunta, Escolha


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
    #resposta = "Voce esta procurando resultados da pergunda %s."
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, 'polls/resultados.html', {'pergunta': pergunta})

def voto(request, pergunta_id):
    p = get_object_or_404(Pergunta, pk=pergunta_id)

    try:
        escolha_selecionada = p.escolha_set.get(pk=request.POST['escolha'])

    except (KeyError, Escolha.DoesNotExist):
        return render(request, 'polls/detalhe.html', {
            'pergunta': p,
            'error_message': "Voce nao escolheu uma opcao",
        })

    else:
        escolha_selecionada.votos += 1
        escolha_selecionada.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:resultados', args=(p.id,)))


    return HttpResponse("voce esta votando da pergunta %s." % pergunta_id)
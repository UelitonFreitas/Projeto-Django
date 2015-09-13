from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from django.views import generic
from polls.models import Pergunta, Escolha


def busca_tadas_as_perguntas_ordenadas_por_data():
    return Pergunta.objects.order_by('-pub_date')[:5]


class IndexView(generic.ListView):

    template_name = 'polls/index.html'
    context_object_name = 'lista_das_ultimas_perguntas'

    def get_queryset(self):
        return Pergunta.objects.order_by('-pub_date')[:5]

class DetalheView(generic.DetailView):

    model = Pergunta
    template_name = 'polls/detalhe.html'

class ResultadosView(generic.DetailView):
    model = Pergunta
    template_name = 'polls/resultados.html'

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
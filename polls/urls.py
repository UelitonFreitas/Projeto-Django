__author__ = 'Ueliton'

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /pools/
    url(r'^$', views.index, name='index'),
    # ex: /pools/5/
    url(r'^(?P<pergunta_id>[0-9]+)/$', views.detalhes, name='detalhe'),
    url(r'^(?P<pergunta_id>[0-9]+)/resultados/$', views.resultados, name='resultados'),
    url(r'^(?P<pergunta_id>[0-9]+)/voto/$', views.voto, name='voto'),

]

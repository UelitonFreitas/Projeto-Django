__author__ = 'Ueliton'

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /pools/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /pools/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetalheView.as_view(), name='detalhe'),
    url(r'^(?P<pk>[0-9]+)/resultados/$', views.ResultadosView.as_view(), name='resultados'),
    url(r'^(?P<pergunta_id>[0-9]+)/voto/$', views.voto, name='voto'),

]

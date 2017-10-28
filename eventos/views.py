from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from eventos.models import *
from eventos.serializers import *

def listaEvento(request):
    retorno = "<h1> Eventos </h1>"
    lista = Evento.objects.all()
    for evento in lista:
        retorno += '</br> Nome do evento: {}'.format(evento.nome)
    return HttpResponse(retorno)

def get_evento_byID(request, id):
    retorno = "<h1> Eventos </h1>"
    evento = Evento.objects.get(pk=id)
    retorno += '</br> Nome do evento: {}'.format(evento.nome)
    return HttpResponse(retorno)

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer







# Create your views here.

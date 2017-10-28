from rest_framework import routers, serializers, viewsets
from eventos.models import *

class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    endereco = EnderecoSerializer(many = False)
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    cliente = ClienteSerializer(many = False)
    class Meta:
        model = Pedido
        fields = '__all__'

class ItemPedidoSerializer(serializers.HyperlinkedModelSerializer):
    pedido = PedidoSerializer(many = False)
    class Meta:
        model = ItemPedido
        fields = '__all__'

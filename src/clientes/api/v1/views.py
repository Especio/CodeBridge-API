from rest_framework import viewsets
from clientes.models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all() #forma de fazer uma consulta padrão. Comandos SQL 
    #filter(estado="MG")
    serializer_class = ClienteSerializer
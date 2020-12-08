from Frontend import models
from rest_framework import viewsets
from API import serializers

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class= serializers.UsuarioSerializer
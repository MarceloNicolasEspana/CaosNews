from rest_framework import serializers
from Frontend import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'


class PeriodistaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Periodista
        fields = '__all__'




from rest_framework import serializers

from artista.models import Artista


class ArtistaSerializer(serializers.ModelSerializer):

    nome = serializers.CharField(required=True)
    genero = serializers.CharField(required=True)

    class Meta:
        model = Artista
        fields = ('id', 'nome', 'genero')
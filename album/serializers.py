from rest_framework import serializers

from album.models import Album


class AlbumSerializer(serializers.ModelSerializer):

    nome = serializers.CharField(required=True)

    class Meta:
        model = Album
        fields = ('id', 'nome', 'artista', 'ano_lancamento', 'faixas')
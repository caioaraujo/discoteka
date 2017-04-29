from rest_framework.response import Response
from rest_framework.views import APIView

from album.models import Album as AlbumModel
from album.serializers import AlbumSerializer
from artista.models import Artista as ArtistaModel
from discoteka.exceptions import RegistroNaoEncontradoException, ValorObrigatorioException


class Album(APIView):

    def post(self, request):
        data = request.data

        self.valida_preenchimento(data)

        artista_id = data.get('artista')
        self.valida_artista(artista_id)

        album = AlbumModel()
        album.nome = data.get('nome')
        album.artista_id = data.get('artista')
        album.ano_lancamento = data.get('ano_lancamento')
        album.faixas = data.get('faixas')
        album.save()

        serializer = AlbumSerializer(album)

        return Response(serializer.data)

    def get(self, request):
        albuns = AlbumModel.objects.filter(artista_id=request.GET.get('artista')).all()

        serializer = AlbumSerializer(albuns, many=True)

        return Response(serializer.data)

    def valida_artista(self, artista_id):
        artista = ArtistaModel.get_artista_por_id(pk=artista_id)

        if not artista:
            raise RegistroNaoEncontradoException("Artista %s não encontrado" % artista_id)

    def valida_preenchimento(self, dados):
        if not dados.get('artista'):
            raise ValorObrigatorioException('Artista é obrigatório')

        if not dados.get('nome'):
            raise ValorObrigatorioException('Nome do álbum é obrigatório')

        if not dados.get('ano_lancamento'):
            raise ValorObrigatorioException('Ano de lançamento é obrigatório')

        if not dados.get('faixas'):
            raise ValorObrigatorioException('Nr. de faixas é obrigatório')


class AlbumId(APIView):

    def delete(self, request, pk):
        pass

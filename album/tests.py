from unittest.mock import MagicMock

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from album.models import Album as AlbumModel
from album.views import Album
from discoteka.exceptions import RegistroNaoEncontradoException, ValorObrigatorioException


class UnitTests(TestCase):
    """ Testes de unidade """

    fixtures = ['artista_fixtures',]

    def test_valida_artista__nao_encontrado(self):
        album = Album()

        with self.assertRaises(RegistroNaoEncontradoException):
            album.valida_artista(99)

    def test_valida_artista__sucesso(self):
        album = Album()

        self.assertIsNone(album.valida_artista(1))

    def test_gera_codigo_gravadora(self):
        album = AlbumModel()

        # Metodo que sincroniza nao nos interessa nesse teste, entao será mockado para nao retornar nada
        album.sincroniza = MagicMock(return_value=None)

        codigo = album.gera_codigo_gravadora_e_sincroniza(album_id=1, artista_id=5)

        self.assertEqual('15', codigo)


class TestesIntegracao(APITestCase):
    """ Testes de integracao """
    fixtures = ['artista_fixtures', 'album_fixtures']

    def setUp(self):
        self.BASE_URL = "/album"

    def test_insercao_sucesso(self):
        data = {'nome': 'Abbey Road', 'artista': 1, 'ano_lancamento': 1968, 'faixas': 17}
        resultado = self.client.post(self.BASE_URL, data)
        self.assertEqual(resultado.status_code, status.HTTP_200_OK)
        self.assertTrue(resultado.data.get('id') > 0)

    def test_insercao__ano_lancamento_obrigatorio(self):
        data = {'nome': 'Darkside of the Moon', 'artista': 2, 'faixas': 11}

        with self.assertRaises(ValorObrigatorioException) as context:
            self.client.post(self.BASE_URL, data)
            self.assertEqual("Ano de lançamento é obrigatório", str(context.exception))

    def test_filtro__albuns_artista_1(self):
        artista = 1
        resultado = self.client.get(self.BASE_URL, {'artista': artista})

        self.assertEqual(resultado.status_code, status.HTTP_200_OK)

        albuns = resultado.data

        for album in albuns:
            self.assertEqual(1, album.get('artista'))




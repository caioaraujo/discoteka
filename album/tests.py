from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

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


class TestesIntegracao(APITestCase):
    """ Testes de integracao """
    fixtures = ['artista_fixtures', 'album_fixtures']

    def setUp(self):
        self.BASE_URL = "/album"

    def test_post_sucesso(self):
        data = {'nome': 'Abbey Road', 'artista': 1, 'ano_lancamento': 1968, 'faixas': 17}
        resultado = self.client.post(self.BASE_URL, data)
        self.assertEqual(resultado.status_code, status.HTTP_200_OK)
        self.assertTrue(resultado.data.get('id') > 0)

    def test_post__ano_lancamento_obrigatorio(self):
        data = {'nome': 'Darkside of the Moon', 'artista': 2, 'faixas': 11}

        with self.assertRaises(ValorObrigatorioException) as context:
            self.client.post(self.BASE_URL, data)
            self.assertEqual("Ano de lançamento é obrigatório", str(context.exception))



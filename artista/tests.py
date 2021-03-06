from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from artista.models import Artista as ArtistaModel
from artista.views import Artista
from discoteka.exceptions import RegistroRedundanteException, ValorObrigatorioException, RegistroNaoEncontradoException


class UnitTests(TestCase):
    """ Testes de unidade """

    fixtures = ["artista_fixtures", ]

    def test_redundacia__falha(self):
        dados = {'nome': 'Pink Floyd', 'genero': 'Rock'}

        with self.assertRaises(RegistroRedundanteException) as context:
            artista = Artista()
            artista.valida_redundancia(dados)
        self.assertEqual('Artista ja cadastrado', str(context.exception))

    def test_redundancia__sucesso(self):
        dados = {'nome': 'Pink Floyd', 'genero': 'Samba'}

        artista = Artista()
        self.assertIsNone(artista.valida_redundancia(dados))


class TestesIntegracao(APITestCase):
    """ Testes de integracao """

    fixtures = ["artista_fixtures",]

    def setUp(self):
        self.BASE_URL = "/artista"

    def test_insercao_sucesso(self):
        data = {'nome': 'Raul Seixas', 'genero': 'Rock'}
        resultado = self.client.post(self.BASE_URL, data)
        self.assertEqual(resultado.status_code, status.HTTP_200_OK)
        self.assertTrue(resultado.data.get('id') > 0)

    def test_insercao__nome_obrigatorio(self):
        data = {'genero': 'Rap'}
        with self.assertRaises(ValorObrigatorioException):
            self.client.post(self.BASE_URL, data)

    def test_filtro_por_genero(self):
        genero = "Rock"
        resultado = self.client.get(self.BASE_URL, {'genero': genero})

        self.assertEqual(resultado.status_code, status.HTTP_200_OK)

        items = resultado.data
        # Assegura que a lista de items veio com pelo menos 1 resultado
        self.assertTrue(len(items))

        for artista in items:
            self.assertEqual(genero, artista.get('genero'))

    def test_busca_total(self):
        resultado = self.client.get(self.BASE_URL)

        self.assertEqual(resultado.status_code, status.HTTP_200_OK)
        self.assertEqual(3, len(resultado.data))

    def test_exclusao__nao_encontrado(self):
        with self.assertRaises(RegistroNaoEncontradoException):
            self.client.delete(self.BASE_URL + '/99')

    def test_exclusao__sucesso(self):
        resultado = self.client.delete(self.BASE_URL + '/3')
        self.assertEqual(resultado.status_code, status.HTTP_200_OK)
        self.assertEqual('Artista removido com sucesso', resultado.data.get('message'))

        # Assegura nao encontrar o objeto na base apos exclusao
        self.assertFalse(ArtistaModel.objects.filter(id=3).first())

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


class UnitTests(TestCase):
    """ Testes de unidade """

    def test_aaa(self):
        pass


class TestesIntegracao(APITestCase):
    """ Testes de integracao """

    def setUp(self):
        self.BASE_URL = "/album"

    def test_post_sucesso(self):
        data = {'nome': 'Revolver'}
        resultado = self.client.post(self.BASE_URL, data)
        self.assertEqual(resultado.status_code, status.HTTP_200_OK)



#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView

from artista.models import Artista as ArtistaModel
from artista.serializers import ArtistaSerializer
from discoteka.exceptions import RegistroRedundanteException, ValorObrigatorioException, RegistroNaoEncontradoException


class Artista(APIView):

    def post(self, request):
        data = request.data

        self.valida_preenchimento(data)
        self.valida_redundancia(data)

        artista = ArtistaModel()
        artista.nome = data.get('nome')
        artista.genero = data.get('genero')
        artista.save()

        serializer = ArtistaSerializer(artista)

        return Response(serializer.data)

    def get(self, request):
        filtro_genero = request.GET.get('genero')

        if filtro_genero:
            artistas = ArtistaModel.objects.filter(genero__icontains=filtro_genero).all()
        else:
            artistas = ArtistaModel.objects.all()

        serializer = ArtistaSerializer(artistas, many=True)

        return Response(serializer.data)

    def valida_preenchimento(self, dados):
        nome_artista = dados.get('nome')
        genero_artista = dados.get('genero')

        if not nome_artista:
            raise ValorObrigatorioException("Nome do artista não informado")

        if not genero_artista:
            raise ValorObrigatorioException("Gênero do artista não informado")

    def valida_redundancia(self, dados):
        nome_artista = dados.get('nome')
        genero_artista = dados.get('genero')

        redundancia = ArtistaModel.objects.filter(nome__icontains=nome_artista, genero__icontains=genero_artista).first()

        if redundancia:
            raise RegistroRedundanteException("Artista ja cadastrado")


class ArtistaId(APIView):

    def delete(self, request, pk):

        artista = ArtistaModel.get_artista_por_id(pk=pk)

        if not artista:
            raise RegistroNaoEncontradoException("Artista não encontrado")

        artista.delete()

        return Response({'message': 'Artista removido com sucesso'}, content_type='application/json')



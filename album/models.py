#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

from artista.models import Artista


class Album(models.Model):
    """ Modelagem dos albuns dos artistas """
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    faixas = models.IntegerField()
    artista = models.ForeignKey(Artista)

    class Meta:
        db_table = 'album'

    @staticmethod
    def get_album_por_id(pk):
        return Album.objects.filter(id=pk).first()

    def gera_codigo_gravadora_e_sincroniza(self, album_id, artista_id):
        codigo = str(album_id) + str(artista_id)

        self.sincroniza(codigo)

        return codigo

    def sincroniza(self, codigo):
        raise Exception('Não implementado')

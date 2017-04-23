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

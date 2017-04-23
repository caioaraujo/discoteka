#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

    class Meta:
        db_table = 'artista'

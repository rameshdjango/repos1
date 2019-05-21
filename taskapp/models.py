# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class imdb(models.Model):
    popularity = models.FloatField(null=True)
    director = models.CharField(max_length=25, null=True, blank=True)
    genre = models.CharField(max_length=25, null=True)
    imdb_score = models.FloatField(null=True)
    name = models.CharField(max_length=100, null=True)


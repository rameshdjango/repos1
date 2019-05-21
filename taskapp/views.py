# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import generics, viewsets
from taskapp.models import imdb
from taskapp.serialaizers import ImdbSerializer
# import django_filters
from django_filters .rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated



class ImdbViewSet(viewsets.ModelViewSet):
    queryset = imdb.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = ImdbSerializer
    filter_fields = ('popularity', 'director', 'genre', 'imdb_score','name')
    search_fields = ('popularity', 'director', 'genre', 'imdb_score','name')

class ListAdmin(generics.ListCreateAPIView):
    queryset = imdb.objects.all()
    serializer_class = ImdbSerializer


class DetailAdmin(generics.RetrieveUpdateDestroyAPIView):
    queryset = imdb.objects.all()
    serializer_class = ImdbSerializer



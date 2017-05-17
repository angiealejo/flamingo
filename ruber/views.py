# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render

# Restframework classes
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# App Models
from .models import Phoenicopterus

# App Serializers
from .serializers import PhoenicopterusSerializer

# Other Apps Utils
from utils.pagination import GenericPagination


class PhoenicopterusViewset(viewsets.ModelViewSet):
    queryset = Phoenicopterus.objects.all().order_by('-id')
    serializer_class = PhoenicopterusSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = (
        'name',
        'description',
        'age',
        'genre'
    )

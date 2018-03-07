# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Restframework classes
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# App Models
from .models import Phoenicopterus

# App Serializers
from .serializers import PhoenicopterusSerializer

# App Filters
from .filters import PhoenicopterusFilter

# Other Apps Utils
from utils.pagination import GenericPagination


# Example of viewset using attribute filter fields
class PhoenicopterusViewSet(viewsets.ModelViewSet):
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


# Example of viewset using attribute filter class
class PhoenicopterusViewSet2(viewsets.ModelViewSet):
    queryset = Phoenicopterus.objects.all().order_by('-id')
    serializer_class = PhoenicopterusSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = PhoenicopterusFilter

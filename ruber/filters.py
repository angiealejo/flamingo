# -*- coding: utf-8 -*-

# Restframework filters
from rest_framework import filters
from django_filters import CharFilter
from django_filters import NumberFilter

# App Models
from .models import Phoenicopterus


class PhoenicopterusFilter(filters.FilterSet):

    name = CharFilter(
        name="name",
        lookup_expr="icontains"
    )
    description = CharFilter(
        name="description",
        lookup_expr="icontains"
    )
    age_min = NumberFilter(
        name="age",
        lookup_expr="gte"
    )
    age_max = NumberFilter(
        name="age",
        lookup_expr="lte"
    )

    class Meta:
        model = Phoenicopterus
        fields = [
            'genre'
        ]

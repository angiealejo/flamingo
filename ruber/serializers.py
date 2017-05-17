# -*- coding: utf-8 -*-

# Restframework Serializers
from rest_framework import serializers

# App Models
from .models import Phoenicopterus


class PhoenicopterusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phoenicopterus
        fields = (
            'url',
            'pk',
            'name',
            'description',
            'age',
            'genre',
            'created_date',
            'updated_date'
        )

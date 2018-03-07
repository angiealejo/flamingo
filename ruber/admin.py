# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Phoenicopterus

from kombu.transport.django import models as kombu_models

@admin.register(Phoenicopterus)
class AdminPhoenicopterus(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'age',
        'genre',
        'created_date',
        'updated_date',
    )

admin.site.register(kombu_models.Message)

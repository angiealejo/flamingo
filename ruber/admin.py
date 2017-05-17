# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Phoenicopterus


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

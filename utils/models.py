# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TimeStamp(models.Model):
    created_date = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        null=True
    )

    class Meta:
        abstract = True

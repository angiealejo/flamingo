# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Other Apps Models
from utils.models import TimeStamp


class Phoenicopterus(TimeStamp):
    GENRE = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    name = models.CharField(max_length=70)
    description = models.TextField()
    age = models.IntegerField(
        blank=True,
        default=0
    )
    genre = models.CharField(
        max_length=1,
        blank=True,
        choices=GENRE
    )

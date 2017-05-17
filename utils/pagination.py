# -*- coding: utf-8 -*-

# Restframework pagination
from rest_framework.pagination import PageNumberPagination


class GenericPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'

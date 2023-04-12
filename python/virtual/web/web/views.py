from django.http import HttpResponse

from django.shortcuts import render
from django.core.cache import cache


def cache(request):
    return cache.clear()

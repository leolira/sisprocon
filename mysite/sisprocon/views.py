from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Saudações. Você está no index da aplicação SisProcon.")

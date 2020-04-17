from django.shortcuts import render

# 実験

from django.http import HttpResponse

def index(request):
    return HttpResponse("実験アプリケーション")

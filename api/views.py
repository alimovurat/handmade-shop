from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from datetime import datetime


def home(request: HttpRequest):
    return HttpResponse('hello')


def time_view(request: HttpRequest):
    return HttpResponse(datetime.now())


def script_view(request: HttpRequest):
    return HttpResponse(render(request, 'homepage.html'))
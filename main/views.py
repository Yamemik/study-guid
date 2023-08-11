from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("main page of site \"study-quest\"")
from django.shortcuts import render
from django.http import HttpResponse




def first(request):
    return HttpResponse('<h1>This Is my firest project in specific urls</h1>')

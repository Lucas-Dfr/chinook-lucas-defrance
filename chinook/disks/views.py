from django.shortcuts import render
from django.http import HttpResponse

def albums_list(request):
    return HttpResponse("List of the albums here soon.")

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return HttpResponse("<h1>Boa noite! Aula Python! - Bruno Bartolomeu.</h1>")

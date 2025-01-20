from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World, you are at blog's index")

def detail(request):
    return HttpResponse("You are viewing post detail page")
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello world, You are at blog's index")

def detail(request,post_id):
    return HttpResponse(f"You are viewing post detail page and Id is {post_id}")
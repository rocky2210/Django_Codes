from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World, you are at blog's index")

def detail(request,post_id):
    return HttpResponse(f"You are viewing post detail page. And Id is {post_id}")

def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(request):
    return HttpResponse("This is the new url")


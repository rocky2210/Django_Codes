from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404

# Create your views here.
# dummy data
# posts = [
#         {'id':1,'title':'post 1', 'content':'content of Post 1'},
#         {'id':2,'title':'post 2', 'content':'content of Post 2'},
#         {'id':3,'title':'post 3', 'content':'content of Post 3'},
#         {'id':4,'title':'post 4', 'content':'content of Post 4'}
#     ]
    
    
def index(request):
    blog_title = "Latest Posts !"
    # Getting data from the post mode
    posts = Post.objects.all()
    return render(request,"blog/index.html",{'blog_title':blog_title,'posts':posts})

def detail(request,slug):
    # Getting static data
    # post = next((item for item in posts if item['id'] == int(post_id)),None)
    
    # Getting data from model by post id
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    # logger = logging.getLogger('Testing')
    # logger.debug(f'post variable is {post}')
    
    return render(request,"blog/detail.html",{'post':post, 'related_posts':related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL")
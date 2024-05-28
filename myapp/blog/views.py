from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post, About_us
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

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
    all_posts = Post.objects.all()
    
    # Paginate
    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"blog/index.html",{'blog_title':blog_title,'page_obj':page_obj})

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

    
def contact_view(request):
    logger = logging.getLogger('Testing')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if form.is_valid():
            logger.debug(f'POST Data is {form.cleaned_data["name"]} {form.cleaned_data["email"]} {form.cleaned_data["message"]}')
            success_message = 'Your email has been sent!'
            return render(request, 'blog/contact.html', {'form': form,'success_message':success_message})
            
        else:
            logger.debug('Form validation failure')
        return render(request, 'blog/contact.html', {'form': form, 'name': name, 'email': email, 'message': message})
    return render(request, 'blog/contact.html')


def about_view(request):
    about_content = About_us.objects.first().content # returns the first content id 
    return render(request,'blog/about.html' , {'about_content': about_content})
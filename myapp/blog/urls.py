from django.urls import path
from . import views 
urlpatterns = [
    path("", views.index,name="index"),
    path("post/<int:post_id>", views.detail,name="detail"),
    path("new_url", views.new_url_view,name="new_url"),
    path("old_url", views.old_url_redirect,name="old_url"),
    
]




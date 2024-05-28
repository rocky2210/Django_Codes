from django.db import models
from django.utils.text import slugify

# Create your models here.

# Category
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE) # many to one relation epolam ena category delete pandropo athu delete agum
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    

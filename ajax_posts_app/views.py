from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'all_posts': Post.objects.all()
    }
    return render(request, 'index.html', context)

def create_post_ajax(request):
    Post.objects.create(content=request.POST['post_content'])
    context ={
        'all_posts': Post.objects.all()
    }
    return render(request, 'post_ajax.html', context)
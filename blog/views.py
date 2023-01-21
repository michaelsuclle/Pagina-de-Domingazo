from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #linea de arriba filtra solo si estan publicados
#    for post in posts:
#        print(post)
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail (request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'posts': posts})


def contact (request):
    return render(request, 'blog/contact.html', {})
 

def about (request):
    return render(request, 'blog/about.html', {})


def sellwithus (request):
    return render(request, 'blog/sellwithus.html', {})
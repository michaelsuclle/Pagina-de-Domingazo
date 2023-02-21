from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.db.models import Q
# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #linea de arriba filtra solo si estan publicados
    queryset = request.GET.get("buscar")
    filtrodetipo = request.GET.get("filtrodetipo")


    if queryset:
        print ("hay query")
        if filtrodetipo:
            posts = Post.objects.filter((
                Q(titulo__icontains = queryset) |
                Q(descripcion__icontains = queryset) |
                Q(ubicacion__icontains = queryset)) & Q(estadodepredio__icontains = filtrodetipo)
            ).distinct()
        else:
            posts = Post.objects.filter((
                            Q(titulo__icontains = queryset) |
                            Q(descripcion__icontains = queryset) |
                            Q(ubicacion__icontains = queryset))
                        ).distinct()
    else:
        if filtrodetipo:
            posts = Post.objects.filter(
                Q(estadodepredio__icontains = filtrodetipo)
            ).distinct()


        

#    for post in posts:
#        print(post)
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail (request, pk):
    post = get_object_or_404(Post, pk=pk)

    ubicaciondelpost = post.ubicacion
    estadodelpost = post.estadodepredio
    ubicaciondelpost = post.titulo

    print ("hay query")
    postsrelacionados = Post.objects.filter(
        Q(ubicacion__icontains = ubicaciondelpost) &
        Q(estadodepredio = estadodelpost)
    ).distinct()

    if (not postsrelacionados):
        postsrelacionados = Post.objects.filter(
            Q(ubicacion__icontains = ubicaciondelpost) |
            Q(estadodepredio = estadodelpost)
        ).distinct()
    return render(request, 'blog/post_detail.html', {'post': post, 'postsrelacionados': postsrelacionados})


def contact (request):
    return render(request, 'blog/contact.html', {})
 

def about (request):
    return render(request, 'blog/about.html', {})


def sellwithus (request):
    return render(request, 'blog/sellwithus.html', {})

def furnitures (request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    queryset = request.GET.get("buscar")
    filtrodetipo = request.GET.get("filtrodetipo")
    if queryset:
        print ("hay query")
        if filtrodetipo:
            posts = Post.objects.filter((
                Q(titulo__icontains = queryset) |
                Q(descripcion__icontains = queryset) |
                Q(ubicacion__icontains = queryset)) & Q(estadodepredio__icontains = filtrodetipo)
            ).distinct()
        else:
            posts = Post.objects.filter((
                            Q(titulo__icontains = queryset) |
                            Q(descripcion__icontains = queryset) |
                            Q(ubicacion__icontains = queryset))
                        ).distinct()
    else:
        if filtrodetipo:
            posts = Post.objects.filter(
                Q(estadodepredio__icontains = filtrodetipo)
            ).distinct()


    
    return render(request, 'blog/furnitures.html', {'posts': posts})

 
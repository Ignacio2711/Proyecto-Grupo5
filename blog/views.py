#from django.http import HttpResponse

# (Walter) Por ahora comento que la linea de arriba se puede eliminar porque
# en la linea de abajo, HttpResponse ya esta importado, por lo tanto
# es inecesaria, por ahora dejo el comentario para que se ubiquen, pero luego
# borramos todo esto.
# El que ve pone su nombre abajo y cuando todos lo vean borramos
#

from django.shortcuts import render
from .form import PostForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from .models import post

# Create your views here.
def index(request):
    return render(request,"blog/index.html",{})


def blog(request):
    return render(request,"blog/blog.html",{})

def noticias(request):
    return render(request,"blog/noticias.html",{})

def post2(request):
    return render(request,'blog/post2.html',{})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def id(request):
    return render(request,"blog/id.html",{})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    Post = get_object_or_404(post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            Post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
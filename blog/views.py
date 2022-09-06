#from django.http import HttpResponse

# (Walter) Por ahora comento que la linea de arriba se puede eliminar porque
# en la linea de abajo, HttpResponse ya esta importado, por lo tanto
# es inecesaria, por ahora dejo el comentario para que se ubiquen, pero luego
# borramos todo esto.
# El que ve pone su nombre abajo y cuando todos lo vean borramos
#

<<<<<<< HEAD
from multiprocessing import context
from django.shortcuts import render
=======
from django.shortcuts import render, redirect, get_object_or_404
>>>>>>> 924408f0fbbf33a5f80b86f129cbca4e70f79a87
from .form import PostForm
from django.views.generic import View
from .models import post



# Create your views here.
def index(request):
    return render(request,"blog/index.html",{})


def blog(request):
<<<<<<< HEAD
    posts = post.objects.all()
    context={
        'posts':posts
    }
    return render(request,"blog/blog.html", context)
=======
    return render(request,"blog.html",{})
>>>>>>> 924408f0fbbf33a5f80b86f129cbca4e70f79a87

def noticias(request):
    return render(request,"blog/noticias.html",{})

def post2(request):
    return render(request,'blog/post2.html',{})

<<<<<<< HEAD
def post_detail(request, pk):
    return render(request, 'blog/post_detail.html', {'post': post})
=======
"""def post_detail(request, pk):
    return render(request, 'blog/post_detail.html', {'post': post})"""
>>>>>>> 924408f0fbbf33a5f80b86f129cbca4e70f79a87

def id(request):
    return render(request,"blog/id.html",{})

def post(request):
    return render(request,'templates/blog/post.html')



"""
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            post = form.save()
=======
>>>>>>> 924408f0fbbf33a5f80b86f129cbca4e70f79a87
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
<<<<<<< HEAD
            post = form.save(commit=False)
=======
>>>>>>> 924408f0fbbf33a5f80b86f129cbca4e70f79a87
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})"""
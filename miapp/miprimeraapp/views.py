from django.shortcuts import render, redirect
from .forms import CategoriaForm, AutorForm, PostForm
from .models import Categoria, Autor, Post
from django.db.models import Q

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'miprimeraapp/base.html')

def insertar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'miprimeraapp/insertar_categoria.html', {'form': form})

def insertar_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'miprimeraapp/insertar_autor.html', {'form': form})

def insertar_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'miprimeraapp/insertar_post.html', {'form': form})

def buscar_post(request):
    query = request.GET.get('q')
    resultados = Post.objects.filter(Q(titulo__icontains=query)) if query else []
    return render(request, 'miprimeraapp/buscar_post.html', {'resultados': resultados, 'query': query})
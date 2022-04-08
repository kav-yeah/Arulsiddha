from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from .models import Post
# Create your views here.
class BlogListview(ListView):
    model=Post
    template_name='blog.html'
class BlogDetailview(DetailView):
    model=Post
    template_name='post-detail.html'
class BlogCreateView(DetailView):
    model=Post
    template_name='post-create.html'
    fields='__all__'

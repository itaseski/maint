from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from.models import Category, Tag, Post

class Home(ListView):
    model = Post
    template_name ='blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog for Something'
        return context

def get_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render (request, 'blog/post.html', {'post': post})


def get_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render (request, 'blog/category.html', {'category': category})


class PostsByCategory(ListView):
    template_name ='blog/index.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.filter(category__slug = self.kwargs('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug = self.kwargs('slug'))
        return context

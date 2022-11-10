from django.shortcuts import render

from django.shortcuts import get_object_or_404, render

from.models import Category


def index(request):
    return render (request, 'blog/index.html')


def get_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render (request, 'blog/category.html', {'category': category})
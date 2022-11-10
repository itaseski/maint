menu:

You can extend the template engine by defining custom tags and filters using Python, and then make them available to your templates using the {% load %} tag.

    from django.shortcuts import get_object_or_404, render

    def get_category(request, slug):
        category = get_object_or_404(Category, slug=slug)
        return render (request, 'blog/category.html', {'category': category})

Во models class Category - метод за апсолутна адреса

    from django.urls import reverse

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug':self.slug})

сега пишуваме кориснички template

The most common place to specify custom template tags and filters is inside a Django app. 
folder blog/templatestag

- the __init__.py file to ensure the directory is treated as a Python package.
- menu.py
- To be a valid tag library, the module must contain a module-level variable named register that is a template.Library instance, in which all the tags and filters are registered. So, near the top of your module, put the following:
- from django import template
- register = template.Library()
  

    from django import template
    from blog.models import Category

    register = template.Library()

    @register.inclusion_tag('blog/menu_tpl.html')
    def show_menu(menu_class='menu'):
        '''Here we'''
        categories = Category.objects.all()
        return {'categories': categories , 'menu_class': menu_class}

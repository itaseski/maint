from django import template
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_menu_header(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories , 'menu_class': menu_class}

@register.inclusion_tag('blog/menu_tfoot.html')
def show_menu_footer(menu_class='footer'):
    categories = Category.objects.all()
    return {'categories': categories , 'menu_class': menu_class}

from django.template import Library
from ..models import Category

register = Library()

@register.inclusion_tag('includes/sidebar.html')
def sidebar_view(category=None):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'category':category
    }

    return context
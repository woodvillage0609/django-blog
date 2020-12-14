from .models import Category, Tag

def related(request):
    context = {
        'blog_category_list': Category.objects.all(),
        'blog_tag_list':Tag.objects.all(),
    }
    return context
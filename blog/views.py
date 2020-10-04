from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def allblog(request):
    object_list = Blog.objects.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, 'blog/allblog.html', {'blogs': blogs, 'page': page})


def detail(request, blog_id):
    detaiBlog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detaiBlog})

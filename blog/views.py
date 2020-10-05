from django.shortcuts import render, get_object_or_404
from .models import Blog,Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm


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
    detailBlog = get_object_or_404(Blog, pk=blog_id)
    comments = detailBlog.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = detailBlog
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/detail.html',
                  {'blog': detailBlog, 'comments': comments, 'new_comments': new_comment, 'comment_form': comment_form})

from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')

def topic_page(request):
    blogs = Blog.objects.filter(is_draft=False)
    return render(request, 'topic_page.html', {'blogs': blogs})

@login_required
def blog_page(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.comments.all()
    return render(request, 'blog_page.html', {'blog': blog, 'comments': comments})
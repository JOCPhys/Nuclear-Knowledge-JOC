from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from allauth.account.forms import SignupForm
from django.contrib.auth.views import LoginView
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.contrib.auth.decorators import login_required

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

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('topic_page')
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

@login_required
def create_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog = blog
            comment.save()
            return redirect('blog_page', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing_page')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
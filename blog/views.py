from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from allauth.account.forms import SignupForm
from django.contrib.auth.views import LoginView
from .models import Topic, Comment
from .forms import TopicForm, CommentForm
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, 'landing_page.html')

def topic_page(request):
    topics = Topic.objects.filter(published=True)
    return render(request, 'topic_page.html', {'topics': topics})

@login_required
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    comments = topic.comments.all()
    return render(request, 'topic_detail.html', {'topic': topic, 'comments': comments})

@login_required
def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect('topic_page')
    else:
        form = TopicForm()
    return render(request, 'create_topic.html', {'form': form})

@login_required
def create_comment(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.topic = topic
            comment.save()
            return redirect('topic_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(request) # Save the user to the database
            backend = 'allauth.account.auth_backends.AuthenticationBackend'
            login(request, user, backend=backend)
            return redirect('landing_page')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
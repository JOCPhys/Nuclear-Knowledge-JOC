from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login
from allauth.account.forms import SignupForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Topic, Comment
from .forms import TopicForm, CommentForm, CommentEditForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def landing_page(request):
    topics = Topic.objects.filter(published=True)
    return render(request, 'landing_page.html', {'topics': topics})

def nuclear_facilities(request):
    topics = Topic.objects.filter(category='nuclear_facilities')
    topics_with_likes = topics.filter(published=True)
    return render(request, 'nuclear_facilities.html', {'topics': topics, 'topics_with_likes': topics_with_likes})

def nuclear_fuel_waste(request):
    topics = Topic.objects.filter(category='nuclear_fuel_waste')
    topics_with_likes = topics.filter(published=True)
    return render(request, 'nuclear_fuel_waste.html', {'topics': topics, 'topics_with_likes': topics_with_likes})

def nuclear_defence(request):
    topics = Topic.objects.filter(category='nuclear_defence')
    topics_with_likes = topics.filter(published=True)
    return render(request, 'nuclear_defence.html', {'topics': topics, 'topics_with_likes': topics_with_likes})

def nuclear_power_space(request):
    topics = Topic.objects.filter(category='nuclear_power_space')
    topics_with_likes = topics.filter(published=True)
    return render(request, 'nuclear_power_space.html', {'topics': topics, 'topics_with_likes': topics_with_likes})

def fact_or_fiction(request):
    topics = Topic.objects.filter(category='fact_or_fiction')
    topics_with_likes = topics.filter(published=True)
    return render(request, 'fact_or_fiction.html', {'topics': topics, 'topics_with_likes': topics_with_likes})

def educational_resources(request):
    topics = Topic.objects.filter(category='educational_resources')
    topics_with_likes = topics.filter(published=True)
    return render(request, 'educational_resources.html', {'topics': topics, 'topics_with_likes': topics_with_likes})

@login_required
def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    comments = Comment.objects.filter(topic=topic, parent__isnull=True)  # Fetch only top-level comments
    topics_with_likes = Topic.objects.filter(published=True).exclude(pk=topic.pk)  # Example for related topics
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")  # Redirect to login if user is not authenticated
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.topic = topic
            comment.save()
            return redirect('topic_detail', slug=slug)
    else:
        form = CommentForm()
    # Order replies for each comment
    for comment in comments:
        comment.ordered_replies = comment.replies.all().order_by('created_at')
    return render(request, 'topic_detail.html', {
        'topic': topic,
        'comments': comments,
        'form': form,
        'like_count': topic.likes.count(),  # Pass the like count to the template
        'topics_with_likes': topics_with_likes,  # Pass related topics to the template
    })

@login_required
@require_POST
def like_topic(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.user in topic.likes.all():
        topic.likes.remove(request.user)
        liked = False
    else:
        topic.likes.add(request.user)
        liked = True
    like_count = topic.likes.count()
    return JsonResponse({'liked': liked, 'like_count': like_count})

@login_required
def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect('topic_detail', slug=topic.slug)
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
            return redirect('topic_detail', slug=topic.slug)
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST' and comment.author == request.user:
        comment.delete()
        return redirect('topic_detail', slug=comment.topic.slug)
    return render(request, 'topic_detail.html', {'topic': comment.topic})

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user != comment.author:
        return redirect('topic_detail', slug=comment.topic.slug)

    if request.method == 'POST':
        form = CommentEditForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('topic_detail', slug=comment.topic.slug)
    else:
        form = CommentEditForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

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
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from allauth.account.forms import SignupForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Topic, Comment
from .forms import TopicForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView

class LandingPageView(ListView):
    model = Topic
    template_name = 'landing_page.html'
    context_object_name = 'topics'
    queryset = Topic.objects.filter(published=True)


class NuclearFacilitiesView(ListView):
    model = Topic
    template_name = 'nuclear_facilities.html'
    context_object_name = 'topics'

    def get_queryset(self):
        return Topic.objects.filter(slug__startswith='nuclear-facilities')


class NuclearFuelWasteView(ListView):
    model = Topic
    template_name = 'nuclear_fuel_waste.html'
    context_object_name = 'topics'

    def get_queryset(self):
        return Topic.objects.filter(slug__startswith='nuclear-fuel-waste')


class NuclearDefenceView(ListView):
    model = Topic
    template_name = 'nuclear_defence.html'
    context_object_name = 'topics'

    def get_queryset(self):
        return Topic.objects.filter(slug__startswith='nuclear-defence')


class NuclearPowerSpaceView(ListView):
    model = Topic
    template_name = 'nuclear_power_space.html'
    context_object_name = 'topics'

    def get_queryset(self):
        return Topic.objects.filter(slug__startswith='nuclear-power-space')


class FactOrFictionView(ListView):
    model = Topic
    template_name = 'fact_or_fiction.html'
    context_object_name = 'topics'

    def get_queryset(self):
        return Topic.objects.filter(slug__startswith='fact-or-fiction')


class EducationalResourcesView(ListView):
    model = Topic
    template_name = 'educational_resources.html'
    context_object_name = 'topics'

    def get_queryset(self):
        return Topic.objects.filter(slug__startswith='educational-resources')


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic_detail.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(topic=self.object, parent__isnull=True)
        context['form'] = CommentForm()
        context['like_count'] = self.object.likes.count()
        return context

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
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('topic_detail', slug=comment.topic.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})

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
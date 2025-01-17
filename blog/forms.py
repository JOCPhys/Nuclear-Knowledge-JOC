from django import forms
from .models import Topic, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'slug', 'content', 'excerpt', 'published', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
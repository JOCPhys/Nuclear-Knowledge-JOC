from django import forms
from .models import Topic, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'slug', 'content', 'excerpt', 'published']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
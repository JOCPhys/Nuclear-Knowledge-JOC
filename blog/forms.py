from django import forms
from .models import Topic, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content', 'is_draft']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
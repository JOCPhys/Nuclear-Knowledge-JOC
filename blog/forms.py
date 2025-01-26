from django import forms
from .models import Topic, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'slug', 'content', 'excerpt', 'published', 'image', 'alt_description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'parent']
        widgets = {
            'parent': forms.HiddenInput()
        }
        
class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html
from .models import Topic, Comment

@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):
    class Media:
        css = {
            'all': (staticfiles_storage.url('css/admin.css'),)
        }

    list_display = ('title', 'slug', 'excerpt', 'created_at', 'updated_at', 'published')
    search_fields = ['title']
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    date_hierarchy = 'created_at'
    actions = ['approve_topics']

    def approve_topics(self, request, queryset):
        queryset.update(published=True)
    approve_topics.short_description = "Approve selected topics"


    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['unpublished_count'] = Topic.objects.filter(published=False).count()
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('topic', 'author', 'body', 'approved', 'created_at', 'updated_at')
    search_fields = ['body']
    list_filter = ('approved', 'created_at')
    date_hierarchy = 'created_at'
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['unapproved_count'] = Comment.objects.filter(approved=False).count()
        return super().changelist_view(request, extra_context=extra_context)
from django.contrib import admin
from .models import Topic, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Topic)
class TopicAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'excerpt', 'created_at', 'updated_at', 'published')
    search_fields = ['title']
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    date_hierarchy = 'created_at'

# Register models to the admin site
admin.site.register(Comment)
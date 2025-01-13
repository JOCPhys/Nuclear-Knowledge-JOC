from django.contrib import admin
from .models import Topic, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Topic)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_at', 'updated_at', 'is_draft')
    search_fields = ['title']
    list_filter = ('is_draft',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    date_hierarchy = 'created_at'

# Register models to the admin site
admin.site.register(Comment)
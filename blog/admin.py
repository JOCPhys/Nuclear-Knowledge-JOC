from django.contrib import admin
from .models import Blog, Comment

# Register models to the admin site
admin.site.register(Blog)
admin.site.register(Comment)
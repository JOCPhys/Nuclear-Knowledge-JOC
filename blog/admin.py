from django.contrib import admin
from .models import Topic, Comment

# Register models to the admin site
admin.site.register(Topic)
admin.site.register(Comment)
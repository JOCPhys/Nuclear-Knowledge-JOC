"""
URL configuration for nuclear_knowledge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views  

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # Include allauth URLs
    path('admin/', admin.site.urls),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('summernote/', include('django_summernote.urls')),
    path('topic/', views.topic_page, name='topic_page'),
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('', include('blog.urls')), # Include the blog app's urls
]

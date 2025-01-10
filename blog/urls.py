from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('topic/', views.topic_page, name='topic_page'),
    path('blog/<int:pk>/', views.blog_page, name='blog_page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('blog/<int:pk>/create_comment/', views.create_comment, name='create_comment'),
]
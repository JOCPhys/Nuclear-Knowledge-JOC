from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='account_signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.landing_page, name='landing_page'),
    path('topic/', views.topic_page, name='topic_page'),
    path('blog/<int:pk>/', views.blog_page, name='blog_page'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('blog/<int:pk>/create_comment/', views.create_comment, name='create_comment'),
]
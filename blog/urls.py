from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='account_signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.landing_page, name='landing_page'),
    path('topic/', views.topic_page, name='topic_page'),
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('create_topic/', views.create_topic, name='create_topic'),
    path('topic/<int:pk>/create_comment/', views.create_comment, name='create_comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('comment/edit/<int:pk>/', views.edit_comment, name='edit_comment'),
    path('like/<int:pk>/', views.like_topic, name='like_topic'),
]
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path(
        'topic/nuclear-facilities/',
        views.nuclear_facilities,
        name='nuclear_facilities'
    ),
    path(
        'topic/nuclear-fuel-waste/',
        views.nuclear_fuel_waste,
        name='nuclear_fuel_waste'
    ),
    path(
        'topic/nuclear-defence/',
        views.nuclear_defence,
        name='nuclear_defence'
    ),
    path(
        'topic/nuclear-power-space/',
        views.nuclear_power_space,
        name='nuclear_power_space'
    ),
    path(
        'topic/fact-or-fiction/',
        views.fact_or_fiction,
        name='fact_or_fiction'
    ),
    path(
        'topic/educational-resources/',
        views.educational_resources,
        name='educational_resources'
    ),
    path(
        'topic/<slug:slug>/detail/',
        views.topic_detail,
        name='topic_detail'
    ),
    path('create_topic/', views.create_topic, name='create_topic'),
    path(
        'topic/<int:pk>/create_comment/',
        views.create_comment,
        name='create_comment'
    ),
    path(
        'comment/<int:pk>/delete/',
        views.delete_comment,
        name='delete_comment'
    ),
    path(
        'edit_comment/<int:pk>/',
        views.edit_comment,
        name='edit_comment'
    ),
    path('like/<int:pk>/', views.like_topic, name='like_topic'),
    path('register/', views.register, name='account_signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls')),
]
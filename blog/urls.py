from django.urls import path
from .views import (
    landing_page,
    nuclear_facilities,
    nuclear_fuel_waste,
    nuclear_defence,
    nuclear_power_space,
    fact_or_fiction,
    educational_resources,
    topic_detail,
    create_topic,
    edit_topic, 
    request_approval, 
    delete_topic, 
    create_comment,
    delete_comment,
    edit_comment,
    like_topic,
    register,
    CustomLoginView
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('topic/nuclear-facilities/', nuclear_facilities, name='nuclear_facilities'),
    path('topic/nuclear-fuel-waste/', nuclear_fuel_waste, name='nuclear_fuel_waste'),
    path('topic/nuclear-defence/', nuclear_defence, name='nuclear_defence'),
    path('topic/nuclear-power-space/', nuclear_power_space, name='nuclear_power_space'),
    path('topic/fact-or-fiction/', fact_or_fiction, name='fact_or_fiction'),
    path('topic/educational-resources/', educational_resources, name='educational_resources'),
    path('topic/<slug:slug>/detail/', topic_detail, name='topic_detail'),
    path('create_topic/', create_topic, name='create_topic'),
    path('topic/<slug:slug>/edit/', edit_topic, name='edit_topic'), 
    path('topic/<slug:slug>/request-approval/', request_approval, name='request_approval'), 
    path('topic/<slug:slug>/delete/', delete_topic, name='delete_topic'),  
    path('topic/<int:pk>/create_comment/', create_comment, name='create_comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete_comment'),
    path('edit_comment/<int:pk>/', edit_comment, name='edit_comment'),
    path('like/<int:pk>/', like_topic, name='like_topic'),
    path('register/', register, name='account_signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
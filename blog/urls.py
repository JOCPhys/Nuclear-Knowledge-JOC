from django.urls import path
from .views import (
    LandingPageView,
    NuclearFacilitiesView,
    NuclearFuelWasteView,
    NuclearDefenceView,
    NuclearPowerSpaceView,
    FactOrFictionView,
    EducationalResourcesView,
    TopicDetailView,
    create_topic,
    create_comment,
    delete_comment,
    edit_comment,
    like_topic,
    register,
    CustomLoginView
)
from .new_views import TopListView, TopDetailView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('topic/nuclear-facilities/', NuclearFacilitiesView.as_view(), name='nuclear_facilities'),
    path('topic/nuclear-fuel-waste/', NuclearFuelWasteView.as_view(), name='nuclear_fuel_waste'),
    path('topic/nuclear-defence/', NuclearDefenceView.as_view(), name='nuclear_defence'),
    path('topic/nuclear-power-space/', NuclearPowerSpaceView.as_view(), name='nuclear_power_space'),
    path('topic/fact-or-fiction/', FactOrFictionView.as_view(), name='fact_or_fiction'),
    path('topic/educational-resources/', EducationalResourcesView.as_view(), name='educational_resources'),
    path('topic/<slug:slug>/detail/', TopicDetailView.as_view(), name='topic_detail'),
    path('create_topic/', create_topic, name='create_topic'),
    path('topic/<int:pk>/create_comment/', create_comment, name='create_comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete_comment'),
    path('edit_comment/<int:pk>/', edit_comment, name='edit_comment'),
    path('like/<int:pk>/', like_topic, name='like_topic'),
    path('register/', register, name='account_signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # new_views.py
    path('toplist/', TopListView.as_view(), name='toplist'),
    path('toplist/<slug:slug>', TopDetailView.as_view(), name='detail'),

]
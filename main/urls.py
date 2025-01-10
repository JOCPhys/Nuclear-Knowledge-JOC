from django.urls import path
from .views import home_page_view

urlpatterns = [
    path('', home_page_view) # does this trailing comma need removing?
]
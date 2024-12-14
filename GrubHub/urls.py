from django.urls import path
from .views import CategoryView
urlpatterns = [
    path('',CategoryView.as_view(),name="home")
]
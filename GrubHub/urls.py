from django.urls import path
from .views import *
urlpatterns = [
    path('',CategoryView.as_view()),
    path('restaurants',RestaurantListView.as_view()),
    path('restaurant/<int:pk>',RestaurantView.as_view())
]
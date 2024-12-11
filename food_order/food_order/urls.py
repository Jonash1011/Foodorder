from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [
    path('api/food-items/', views.food_items, name='food_items'),
]


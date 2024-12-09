from django.http import JsonResponse
from .models import FoodItem

def food_items(request):
    # Query for all food items (ensure you have a FoodItem model)
    items = FoodItem.objects.all()
    food_list = list(items.values('name', 'price', 'image_url'))
    return JsonResponse(food_list, safe=False)

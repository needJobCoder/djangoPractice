from django.urls import path
from .views import recipe_view, get_recipe_data, get_api_index_data

urlpatterns = [
    path('recipe/', recipe_view),
    path('getRecipes/', get_recipe_data),
    path('getIndex/<int:index>/', get_api_index_data)
]
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .serializer import RecipeSerializer
# Create your views here.
from .serializer import RecipeSerializer
from .models import Recipe

@api_view(['GET', 'POST'])
def recipe_view(request):
    if request.method == "GET":
        return Response({"message": "Hello World GET"})
    elif request.method == "POST":
        recipe_serializer = RecipeSerializer(data=request.data)
        if recipe_serializer.is_valid():
            print(recipe_serializer)
            recipe_serializer.save()
        return Response({"message": "Hello World POST", "receivedData": request.data})

@api_view(["GET"])
def get_api_index_data(request, index):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    recipe_list = []  # Changed variable name here
    for recipe in serializer.data:
        if recipe['id'] == index:
            print(recipe['id'], str(index))
            return Response(
                {"id": recipe['id'], "title": recipe['title'], "description": recipe['description']}
            )
    return Response({"found":"None"})
@api_view(["GET"])
def get_recipe_data(request):
    if request.method == "GET":
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        recipe_list = []  # Changed variable name here
        for recipe in serializer.data:
            recipeObject = {"id": str(recipe['id']), "title": str(recipe['title']), "description": str(recipe['description'])}  # Accessing dictionary values
            print(recipeObject)
            recipe_list.append(recipeObject)
        # data = json.dumps(recipe_list)  # Using the new variable here
        return Response(recipe_list)
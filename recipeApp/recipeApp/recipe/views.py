from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
        return Response({"message": "Hello World POST", "receivedData": request.data})


@api_view(["GET"])
def get_recipe_data(request):
    if request.method == "GET":
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response({"data": serializer.data})


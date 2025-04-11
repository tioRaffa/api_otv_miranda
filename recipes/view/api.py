from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from ..models import Recipe
from ..serializers import RecipeSerializer, AuthorSerializer


@api_view()
def recipes_api_list(request):
    
    recipes = Recipe.objects.get_published()[:10]
    serializer = RecipeSerializer(instance=recipes, many=True, context={'request': request})
    
    return Response(serializer.data)


@api_view()
def recipe_api_detail(request, pk):
    
    recipe = get_object_or_404(Recipe, id=pk)
    serializer = RecipeSerializer(instance=recipe, context={'request': request})
    
    return Response(serializer.data)


@api_view()
def recipe_api_author(request, pk):
    
    author = get_object_or_404(User, pk=pk)
    serializer = AuthorSerializer(instance=author)
    
    return Response(serializer.data)
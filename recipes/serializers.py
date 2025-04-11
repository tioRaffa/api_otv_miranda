from rest_framework import serializers
from django.contrib.auth.models import User
from recipes.models import Recipe
from tag.models import Tag

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'category',
            'slug', 'author', 'author_link', 'preparation',
            'serving', 'preparation_steps', 'preparation_steps_is_html', 'tags',
            'created_at', 'updated_at', 'is_published' ,
        ]
    
    preparation = serializers.SerializerMethodField(read_only=True)
    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} - {recipe.preparation_time_unit}'
    
    serving = serializers.SerializerMethodField(read_only=True)
    def get_serving(self, recipe):
        return f'{recipe.servings} - {recipe.servings_unit}'
    
    category = serializers.StringRelatedField(read_only=True) # Nome da categoria
    
    author = serializers.StringRelatedField(read_only=True)
    author_link = serializers.HyperlinkedRelatedField(
        many=False,
        source='author',
        view_name='recipes:recipe_api_v2_author',
        read_only=True
    )
    

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {
            'email': {'write_only': True},
            'password': {'write_only': True}
        }
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]
    
    
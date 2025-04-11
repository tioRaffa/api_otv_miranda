from rest_framework import serializers
from django.contrib.auth.models import User
from tag.models import Tag

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=244)
    description = serializers.CharField(max_length=165)
    slug = serializers.SlugField()
    
    preparation = serializers.SerializerMethodField()
    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} - {recipe.preparation_time_unit}'
    
    serving = serializers.SerializerMethodField()
    def get_serving(self, recipe):
        return f'{recipe.servings} - {recipe.servings_unit}'
    
    preparation_steps = serializers.CharField()
    preparation_steps_is_html = serializers.BooleanField(default=False)
    
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all()               ID da categoria
    # )
    category = serializers.StringRelatedField() # Nome da categoria
    author = serializers.StringRelatedField()
    
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True
    )
    
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=False)
    
    
    
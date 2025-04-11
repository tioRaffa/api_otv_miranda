from rest_framework import serializers

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=244)
    description = serializers.CharField(max_length=165)
    slug = serializers.SlugField()
    preparation_time = serializers.IntegerField()
    preparation_time_unit = serializers.CharField(max_length=65)
    servings = serializers.IntegerField()
    servings_unit = serializers.CharField(max_length=65)
    preparation_steps = serializers.CharField()
    preparation_steps_is_html = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=False)
from django.urls import path

from recipes import view as views

app_name = 'recipes'


urlpatterns = [
    path(
        '',
        views.RecipeListViewHome.as_view(),
        name="home"
    ),
    path(
        'recipes/search/',
        views.RecipeListViewSearch.as_view(),
        name="search"
    ),
    path(
        'recipes/tags/<slug:slug>/',
        views.RecipeListViewTag.as_view(),
        name="tag"
    ),
    path(
        'recipes/category/<int:category_id>/',
        views.RecipeListViewCategory.as_view(),
        name="category"
    ),
    path(
        'recipes/<int:pk>/',
        views.RecipeDetail.as_view(),
        name="recipe"
    ),
    path(
        'recipes/api/v1/',
        views.RecipeListViewHomeApi.as_view(),
        name="recipes_api_v1",
    ),
    path(
        'recipes/api/v1/<int:pk>/',
        views.RecipeDetailAPI.as_view(),
        name="recipes_api_v1_detail",
    ),
    path(
        'recipes/theory/',
        views.theory,
        name='theory',
    ),
    path(
        'api/v2/recipes/',
        views.api.recipes_api_list,
        name='recipes_api_v2'
    ),
    path(
        'api/v2/recipe/<int:pk>',
        views.api.recipe_api_detail,
        name='recipe_api_v2_detail'
    ),
    path(
        'api/v2/recipe/author/<int:pk>/',
        views.api.recipe_api_author,
        name='recipe_api_v2_author'
    )

]

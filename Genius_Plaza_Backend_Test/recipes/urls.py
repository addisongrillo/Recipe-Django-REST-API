from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('recipes', views.RecipeView)
router.register('steps', views.StepView)
router.register('ingredients', views.IngredientView)

urlpatterns = [
    path('', include(router.urls))
]

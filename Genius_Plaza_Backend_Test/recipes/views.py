from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Recipe, Step, Ingredient
from .serializers import UserSerializer, RecipeSerializer, StepSerializer, IngredientSerializer
from django.db.models import Q


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Recipe.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(user__username__icontains=query)
            ).distinct()
        return queryset_list

class StepView(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
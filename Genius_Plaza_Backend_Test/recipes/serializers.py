from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipe, Step, Ingredient

class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'url', 'step_text', 'recipe')

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'url', 'text', 'recipe')

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    recipe_ingredients = IngredientSerializer(many=True, required=False, allow_null=True)
    recipe_steps = StepSerializer(many=True, required=False, allow_null=True)
    def update(self, instance, validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.user = validated_data.get('user', instance.user)
        return instance
    class Meta:
        model = Recipe
        fields = ('url', 'id', 'name', 'user', 'recipe_ingredients', 'recipe_steps')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_recipes = RecipeSerializer(many=True, required=False, allow_null=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', 'password', 'user_recipes')
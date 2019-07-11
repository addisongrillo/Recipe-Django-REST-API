from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_recipes", null=True)

    def __str__(self):
        return self.name

class Step(models.Model):
    step_text = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_steps")

    def __str__(self):
        return self.step_text

class Ingredient(models.Model):
    text = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")

    def __str__(self):
        return self.text


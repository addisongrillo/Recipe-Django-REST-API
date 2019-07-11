# Recipes API

## Description

The Recipes API can be used to Store Recipes, Ingredients and Steps for making delicious meals.

### Get all Recipes

GET

http://localhost:8000/recipes/

###Search Recipes by user

Recipes can be searched for by username, User first name, and User Last Name

Example:

GET

http://localhost:8000/recipes/?q={username}

###Search Recipes by Recipe name

http://localhost:8000/recipes/?q={recipe name or part of recipe name}

### Get a Recipe by id

GET

http://localhost:8000/recipes/{id}/

### Create a Recipe

POST

http://localhost:8000/recipes/

body:
{
	"name": "recipe name",
    "user": "http://localhost:8000/users/{id}/"
}

### Update a Recipe

PUT

http://localhost:8000/recipes/{id}/

body:
{
    "name": "{recipe name}",
    "user": "http://localhost:8000/users/{id}/",
    "recipe_ingredients": [],
    "recipe_steps": []
}

### Delete a Recipe

DELETE

http://localhost:8000/recipes/{id}/

### Get a Step by id

GET

http://localhost:8000/steps/{id}/

### Create a Step

POST

http://localhost:8000/steps/

body:
{
    "step_text": "{step text}",
    "recipe": "http://localhost:8000/recipes/{id}"
}

### Update a Step

PUT

http://localhost:8000/steps/{id}/

body:
{
    "step_text": "{step text}",
    "recipe": "http://localhost:8000/recipes/{id}"
}

### Delete a Step

DELETE

http://localhost:8000/steps/{id}/

### Get an Ingredient by id

GET

http://localhost:8000/steps/{id}/

### Create an Ingredient

POST

http://localhost:8000/ingredients/

body:
{
    "text": "{ingredient text}",
    "recipe": "http://localhost:8000/recipes/{id}"
}

### Update an Ingredient

PUT

http://localhost:8000/ingredients/{id}/

body:
{
    "text": "{ingredient text}",
    "recipe": "http://localhost:8000/recipes/{id}"
}

### Delete an Ingredient

DELETE

http://localhost:8000/ingredients/{id}/

### Get a User by id

GET

http://localhost:8000/users/{id}/

### Create a User

POST

http://localhost:8000/users/

body:
{
    "username": "{username}",
    "email": "{email}",
    "first_name": "{first_name}",
    "last_name": "{last_name}",
    "password": "{password}",
    "user_recipes": []
}

### Update a User

PUT

http://localhost:8000/users/{id}/

body:
{
    "username": "{username}",
    "email": "{email}",
    "first_name": "{first_name}",
    "last_name": "{last_name}",
    "password": "{password}",
    "user_recipes": []
}

### Delete a User
DELETE

http://localhost:8000/users/{id}/
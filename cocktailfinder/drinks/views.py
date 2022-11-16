from django.shortcuts import render
import requests
from .models import Drink

# Create your views here.
def drink(request, drink_id):
    drinkURL = 'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=' + str(drink_id)
    drinkData = requests.get(drinkURL).json()
    drink = drinkData['drinks']
    drink = drink[0]
    ingredients =[]
    ingredientPortions = []
    for i in range(1,15):
        ingredients.append(drink['strIngredient' + str(i)])
        ingredients =[i for i in ingredients if i is not None]
        ingredientPortions.append(drink['strMeasure' + str(i)])
        ingredientPortions =[i for i in ingredientPortions if i is not None]
    drink['ingredients'] = ingredients
    drink['ingredientPortions'] = ingredientPortions


    if request.method == "POST":
        drinkToAdd = Drink(name=drink['strDrink'],drinkId=drink['idDrink'], instructions=drink['strInstructions'] , note='')
        drinkToAdd.setIngredients(ingredients, ingredientPortions)
        drinkToAdd.save()
        return render(request, 'drinks/drink.html', {'drink':drink})
    else:
        return render(request, 'drinks/drink.html', {'drink':drink})

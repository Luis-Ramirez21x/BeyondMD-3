from django.shortcuts import render, redirect
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
        drinkToAdd = Drink(name=drink['strDrink'],drinkId=drink['idDrink'],imageUrl=drink['strDrinkThumb'], instructions=drink['strInstructions'] , note='')
        drinkToAdd.setIngredients(ingredients, ingredientPortions)
        drinkToAdd.save()
        return render(request, 'drinks/drink.html', {'drink':drink, 'saved': True})
    else:
        return render(request, 'drinks/drink.html', {'drink':drink})
        
def savedDrinks(request):
        savedDrinks_list = Drink.objects.all()

        return render(request, 'drinks/savedDrinks.html', {'savedDrinks': savedDrinks_list})

def addNote(request, drink_id):

    drink = Drink.objects.get(drinkId=drink_id)

    if request.method == "POST":
        userInput = request.POST['userInput']
        drink.note = userInput
        drink.save()

        return render(request, 'drinks/addNote.html',{'drink': drink})
    else:
        return render(request, 'drinks/addNote.html',{'drink': drink})

def deleteDrink(request, drink_id):
    drink = Drink.objects.get(drinkId=drink_id)
    drink.delete()

    return redirect(savedDrinks)

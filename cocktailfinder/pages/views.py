from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    if request.method == "POST":
        userInput = request.POST['userInput']
        searchOption = request.POST.getlist('searchOption')
        apiURL = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?' + searchOption[0] + '=' + userInput
        #dictionary
        response = requests.get(apiURL).json()
        #list
        drinks = response['drinks']
        #dictionary
        for drink in drinks:
            ingredients =[]
            ingredientPortions = []
            for i in range(1,15):
                ingredients.append(drink['strIngredient' + str(i)])
                ingredients =[i for i in ingredients if i is not None]
                ingredientPortions.append(drink['strMeasure' + str(i)])
                ingredientPortions =[i for i in ingredientPortions if i is not None]
            drink['ingredients'] = ingredients
            drink['ingredientPortions'] = ingredientPortions
        
        return render(request, 'pages/index.html', {'drinks':drinks})
    else:
        return render(request, 'pages/index.html')



from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    if request.method == "POST":
        userInput = request.POST['userInput']
        apiURL = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + userInput
        #dictionary
        response = requests.get(apiURL).json()
        #list
        drinks = response['drinks']
        
           
        return render(request, 'pages/index.html', {'drinks':drinks})

    else:
        return render(request, 'pages/index.html')



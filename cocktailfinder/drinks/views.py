from django.shortcuts import render

# Create your views here.
def savedDrinks(request):
    return render(request, 'drinks/savedDrinks.html') 
def searchResults(request):
    return render(request, 'drinks/searchResults.html')
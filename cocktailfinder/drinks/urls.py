from django.urls import path

from . import views
#thought of as routing

urlpatterns = [
    #path('', views.savedDrinks, name='savedDrinks'),
    path('<int:drink_id>', views.drink, name='drink')
]
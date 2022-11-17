from django.urls import path

from . import views
#thought of as routing

urlpatterns = [
    #path('', views.savedDrinks, name='savedDrinks'),
    path('<int:drink_id>', views.drink, name='drink'),
    path('saved-drinks', views.savedDrinks, name='savedDrinks'),
    path('add-note/<str:drink_id>', views.addNote, name='addNote'),
    path('delete-drink/<str:drink_id>', views.deleteDrink, name='deleteDrink')
]
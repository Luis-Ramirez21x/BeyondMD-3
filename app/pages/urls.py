from django.urls import path

from . import views
#thought of as routing

urlpatterns = [
    path('', views.index, name='index'),
   
]
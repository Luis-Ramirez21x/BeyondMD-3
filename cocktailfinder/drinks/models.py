from django.db import models
import json

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=200)
    drinkId= models.CharField(max_length=200)
    instructions = models.TextField(max_length=3000)
    ingredients = models.TextField(max_length=2000)
    ingredientPortions = models.TextField(max_length=2000)
    note = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.name

    def setIngredients (self, ing, ingp):
        self.ingredients = json.dumps(ing)
        self.ingredientPortions = json.dumps(ingp)
    
    def getIngredients (self):
        return json.loads(self.ingredients)

    def getIngredientPortions (self):
        return json.loads(self.ingredientPortions)
    
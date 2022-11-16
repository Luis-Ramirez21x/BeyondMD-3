from django.db import models
import json

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=200)
    instructions = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    note = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def setIngredients (self, lst):
        self.ingredients = json.dumps(lst)
    
    def getIngredients (self):
        return json.loads(self.ingredients)
    
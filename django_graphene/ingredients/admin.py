from django.contrib import admin
from ingredients.models import Ingredient, Category

@admin.register(Ingredient)
class Ingredient(admin.ModelAdmin):
    pass

@admin.register(Category)
class Category(admin.ModelAdmin):
    pass


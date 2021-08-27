import random

import factory.django
from faker import Faker
from ingredients.models import Category, Ingredient

fake = Faker()

ingredient_names = [
    "Banana",
    "Pineapple",
    "Onion",
    "Strawberry",
    "Potato",
    "Egg",
    "Orange Juice",
    "Tomato",
    "Milk",
]

category_names = ["Meat", "Fruit", "Vegetable", "Dairy"]


class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient

    name = random.choice(ingredient_names)
    notes = fake.text()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = random.choice(category_names)

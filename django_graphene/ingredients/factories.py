import random

import factory.django
from faker import Faker
from ingredients.models import Ingredient

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


class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient

    name = random.choice(ingredient_names)
    notes = fake.text()

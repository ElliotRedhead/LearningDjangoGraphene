import pytest
from ingredients.factories import IngredientFactory


@pytest.mark.django_db
class TestModels:
    def test_ingredient_create(self):

        ingredient = IngredientFactory()
        print(ingredient)

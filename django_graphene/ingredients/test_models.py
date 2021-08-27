import pytest
from ingredients.factories import CategoryFactory, IngredientFactory


@pytest.mark.django_db
class TestIngredientModel:
    def test_ingredient_create_without_category(self):
        ingredient = IngredientFactory()
        assert type(ingredient.name) is str
        assert type(ingredient.notes) is str
        assert ingredient.category is None
        assert ingredient.__str__() == ingredient.name


@pytest.mark.django_db
class TestCategoryModel:
    def test_category_create(self):
        category = CategoryFactory()
        assert type(category.name) is str
        assert category.__str__() == category.name

# Create fixture using the graphql_query helper & `client` fixture from `pytest-django`.
import json

import pytest
from graphene_django.utils.testing import graphql_query


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client, graphql_url="/graphql")

    return func


# Test you query using the client_query fixture
@pytest.mark.django_db
def test_ingredients_empty_get(client_query):
    response = client_query(
        """
        query {
            allIngredients {
                id
                name
                notes
            }
        }
        """
    )

    expected_data = {"allIngredients": []}

    actual_content = json.loads(response.content)
    actual_data = actual_content["data"]
    assert "errors" not in actual_content
    assert expected_data == actual_data

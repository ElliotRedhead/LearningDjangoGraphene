import graphene
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredient


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


class IngredientMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        name = graphene.String()
        notes = graphene.String()
        category = graphene.String()
        id = graphene.ID()

    # The class attributes define the response of the mutation
    ingredient = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls, root, info, id, **kwargs):

        ingredient = Ingredient.objects.get(pk=id)

        name = kwargs.get("name", None)
        notes = kwargs.get("notes", None)
        category = kwargs.get("category", None)

        if name is not None:
            ingredient.name = name
        if notes is not None:
            ingredient.notes = notes
        if category is not None:
            ingredient.category = category

        ingredient.save()
        # return an instance of this mutation
        return IngredientMutation(ingredient=ingredient)


class Mutation(graphene.ObjectType):
    update_ingredient = IngredientMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

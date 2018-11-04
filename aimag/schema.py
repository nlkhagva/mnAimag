# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType

from aimag.models import Aimag, Sum


class AimagType(DjangoObjectType):
    class Meta:
        model = Aimag


class SumType(DjangoObjectType):
    class Meta:
        model = Sum


class Query(object):
    all_aimag = graphene.List(AimagType)
    all_sum = graphene.List(SumType)
    aimag = graphene.Field(AimagType,
                              id=graphene.Int(),
                              name=graphene.String())
    sum = graphene.Field(SumType,
                              id=graphene.Int(),
                              name=graphene.String())
    def resolve_all_aimag(self, info, **kwargs):
        return Aimag.objects.all()

    def resolve_all_sum(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Sum.objects.all()

    def resolve_aimag(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Aimag.objects.get(pk=id)

        if name is not None:
            return Aimag.objects.get(name=name)

        return None

    def resolve_sum(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Sum.objects.get(pk=id)

        if name is not None:
            return Sum.objects.get(name=name)

        return None
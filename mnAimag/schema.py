import graphene

import aimag.schema


class Query(aimag.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(aimag.schema.Mutation,graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
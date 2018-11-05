# cookbook/ingredients/schema.py
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from aimag.models import Aimag, Sum



class AimagType(DjangoObjectType):
    class Meta:
        model = Aimag
        filter_fields = {
            'name':['exact','icontains','istartswith'],
        }
        interfaces = (graphene.relay.Node, )


class SumType(DjangoObjectType):
    class Meta:
        model = Sum


class AimagInput(graphene.InputObjectType):
    name = graphene.String(required=False)
    aimag_tuv = graphene.String(required=False)
    hun_am = graphene.Int(required=False)
    id = graphene.String(required=False)

class CreateAimag(graphene.Mutation):
    
    aimag = graphene.Field(AimagType)
    class Arguments:
        aimag_data = AimagInput(required=True)

    @staticmethod
    def mutate(self,info,aimag_data= None):
        print(aimag_data)
        aimag = Aimag(name=aimag_data.name,aimag_tuv = aimag_data.aimag_tuv, hun_am= aimag_data.hun_am)
        aimag.save()
        print(aimag)
        return CreateAimag( aimag = aimag )

class UpdateAimag(graphene.Mutation):
    aimag = graphene.Field(AimagType)
    class Arguments:
        aimag_data = AimagInput(required = True)

    @staticmethod
    def mutate(self,info,aimag_data=None):
        print(aimag_data)
        aimag = Aimag.objects.get(name=aimag_data.name)
        aimag.aimag_tuv = aimag_data.aimag_tuv
        aimag.save()
        print(aimag)
        return UpdateAimag(aimag = aimag)

class Mutation(graphene.AbstractType):
    create_aimag = CreateAimag.Field()
    update_aimag = UpdateAimag.Field()

class Query(object):

    aimag = graphene.relay.Node.Field(AimagType)
    all_aimags = DjangoFilterConnectionField(AimagType)


    # all_aimag = graphene.List(AimagType)
    # all_sum = graphene.List(SumType)
    # aimag = graphene.Field(AimagType,
    #                           id=graphene.Int(),
    #                           name=graphene.String())
    # sum = graphene.Field(SumType,
    #                           id=graphene.Int(),
    #                           name=graphene.String())

                              
    # def resolve_all_aimag(self, info, **kwargs):
    #     return Aimag.objects.all()

    # def resolve_all_sum(self, info, **kwargs):
    #     # We can easily optimize query count in the resolve method
    #     return Sum.objects.all()

    # def resolve_aimag(self, info, **kwargs):
    #     id = kwargs.get('id')
    #     name = kwargs.get('name')

    #     if id is not None:
    #         return Aimag.objects.get(pk=id)

    #     if name is not None:
    #         return Aimag.objects.get(name=name)

    #     return None

    # def resolve_sum(self, info, **kwargs):
    #     id = kwargs.get('id')
    #     name = kwargs.get('name')

    #     if id is not None:
    #         return Sum.objects.get(pk=id)

    #     if name is not None:
    #         return Sum.objects.get(name=name)

    #     return None




# mutation{
#   createAimag(aimagData:{name:"enkhjinqwe",aimagTuv:"dornodqwe",hunAm:11}){
#     aimag{
#       name
#       hunAm
#       aimagTuv
#     }
    
#   }
# }

# mutation{
#   updateAimag(aimagData:{name:"enkhjinqwe",aimagTuv:"enkhjinshdeas",hunAm:11}){
#     aimag{
#       name
#     }
#   }
# }

# query{
#   allAimags(name_Istartswith:"qaa"){
#     edges{
#       node{
#         name
#         id
#         sumSet {
#           name
#         }
#       }
#     }
#   }
#   aimag(id:"QWltYWdUeXBlOjI="){
#     name
#     id
#   }
  
# }
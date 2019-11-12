
from graphene import ObjectType, String
from graphene.types.datetime import DateTime
from graphene.types.json import JSONString

class Query(ObjectType):
    name = String()

    @staticmethod
    def resolve_name(parent, info):
        return 'DataUSA Economic Data Can Be Returned Here'


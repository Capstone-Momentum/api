
from graphene import ObjectType, String
from graphene.types.datetime import DateTime
from graphene.types.json import JSONString

class Query(ObjectType):
    acs1_variable = String()

    @staticmethod
    def resolve_acs1_variable(parent, info):
        return ''



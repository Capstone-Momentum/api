
import json
from graphene import ObjectType, String, Int
from graphene.types.json import JSONString
from dbal.census.acs.query import get_item
from dbal.util import json_serialize

class Query(ObjectType):
    acs1_variable = JSONString(tableName=String(required=True),
                           variableName=String(required=True),
                           year=Int(required=True))

    @staticmethod
    def resolve_acs1_variable(parent, info, tableName, variableName, year):
        item = get_item(tableName, variableName, year)
        return json.dumps(item, default=json_serialize) if (item) else None




import json
from graphene import ObjectType, String
from graphene.types.json import JSONString
from dbal.util import scan_table as scan, json_serialize

class Query(ObjectType):
    data_sources = JSONString()
    scan_table = JSONString(tableName=String())

    @staticmethod
    def resolve_data_sources(parent, info):
        return json.dumps(scan('data_sources'))

    @staticmethod
    def resolve_scan_table(parent, info, tableName):
        return json.dumps(scan(tableName), default=json_serialize)


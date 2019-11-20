
import json
from graphene import ObjectType, String, Int, List
from graphene.types.json import JSONString
from dbal.util import scan_table
from dbal.util import json_serialize

class DatasetItem(ObjectType):
    dataset_names = List(String, title=String(required=True))
    description = String(title=String(required=True))
    geography_link = String(title=String(required=True))
    groups_link = String(title=String(required=True))
    source_path = List(JSONString, title=String(required=True))
    vintage = Int(title=String(required=True))

    @staticmethod
    def resolve_description(parent, info, title):
        pass

class Query(ObjectType):
    dataset_item = DatasetItem()
    all_dataset_items = JSONString()

    @staticmethod
    def resolve_all_dataset_items(parent, info):
        return json.dumps(scan_table('census_datasets'), default=json_serialize)



from boto3_wrapper.dynamodb import get_table
from decimal import Decimal

def json_serialize(obj):
    """JSON serializer for objects not serializable by default json code"""
    if (isinstance(obj, Decimal)):
        return float(obj)
    raise TypeError ("Type %s not serializable" % type(obj))

def scan_table(name):
    table = get_table(name)
    response = table.scan(Select='ALL_ATTRIBUTES')
    try:
        return response['Items']
    except:
        return None

if __name__ == '__main__':
    print(scan_table('census_datasets'))

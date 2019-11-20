
from boto3_wrapper.dynamodb import get_table
from boto3.dynamodb.conditions import Key, Attr

def get_all_dataset_items():
    table = get_table('census_datasets')
    response = table.scan(Select='ALL_ATTRIBUTES')
    try:
        return response['Items']
    except:
        return None


if __name__ == '__main__':
    print(get_all_dataset_items())



import boto3
from data_retrieval.census.constants import VARIABLES_TABLE_NAME_BASE

# DynamoDB Data Types: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.DataTypes.html

def get_table_name(year, acs_table_type):
    return "{}_{}_{}".format(VARIABLES_TABLE_NAME_BASE, str(year), acs_table_type)

def create_variables_table(year, acs_table_type):
    dynamodb = boto3.resource('dynamodb')
    tableName = get_table_name(year, acs_table_type)
    table = dynamodb.create_table(
        TableName=tableName,
        KeySchema=[
            {
                'AttributeName': 'variable_name',
                'KeyType': 'HASH' # aka: the partition key (like primary key, but for NoSQL)
            },
            {
                'AttributeName': 'group',
                'KeyType': 'RANGE' # aka: the sort key (AWS store's the data in this order on their hardware)
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'variable_name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'group',
                'AttributeType': 'S'
            },
            # Columns that exist, but doesn't get defined in the schema:
            # {
            #     'AttributeName': 'label',
            #     'AttributeType': 'S'
            # },
            # {
            #     'AttributeName': 'concept',
            #     'AttributeType': 'S'
            # },
            # {
            #     'AttributeName': 'attributes',
            #     'AttributeType': 'SS'
            # },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName=tableName)

def create():
    pass

if __name__ == '__main__':
    pass


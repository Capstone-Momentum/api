
import boto3
from data_retrieval.census.constants import ACS_TABLE_NAME_BASE, ACS_TABLE_TYPES

# DynamoDB Data Types: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.DataTypes.html

def get_table_name(acs_table_type):
    return "{}_{}".format(ACS_TABLE_NAME_BASE, acs_table_type if (acs_table_type) else 'detailed')

def create_acs_table(acs_table_type):
    dynamodb = boto3.resource('dynamodb')
    tableName = get_table_name(acs_table_type)
    table = dynamodb.create_table(
        TableName=tableName,
        KeySchema=[
            {
                'AttributeName': 'variable_name',
                'KeyType': 'HASH' # aka: the partition key (like primary key, but for NoSQL)
            },
            {
                'AttributeName': 'year',
                'KeyType': 'RANGE' # aka: the sort key (AWS store's the data in this order on their hardware)
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'variable_name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            # Columns that exist, but don't get defined in the schema:
            # {
            #     'AttributeName': 'group',
            #     'AttributeType': 'S'
            # },
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
            # {
            #     'AttributeName': 'california',
            #     'AttributeType': 'SS'
            # },
            # {
            #     'AttributeName': 'slo_county',
            #     'AttributeType': 'SS'
            # },
        ],

        # Keeps us free-tier eligible
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait for table to be created
    # table.meta.client.get_waiter('table_exists').wait(TableName=tableName)

def create():
    for tableType in ACS_TABLE_TYPES:
        try:
            create_acs_table(tableType)
        except:
            continue

if __name__ == '__main__':
    create()


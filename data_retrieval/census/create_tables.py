

from boto3_wrapper.dynamodb import create_table
from constants.census.constants import ACS_TABLE_NAME_BASE, ACS_TABLE_TYPES

# DynamoDB Data Types: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.DataTypes.html

def create_census_datasets_table():
    tableName = 'census_datasets'
    table = create_table(dict(
        TableName=tableName,
        KeySchema=[
            {
                'AttributeName': 'title',
                'KeyType': 'HASH' # aka: the partition key (like primary key, but for NoSQL)
            },
            {
                'AttributeName': 'dataset_names',
                'KeyType': 'RANGE' # aka: the sort key (AWS store's the data in this order on their hardware)
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'dataset_names',
                'AttributeType': 'S'
            },
            # Columns that exist, but don't get defined in the schema:
            # {
            #     'AttributeName': 'description',
            #     'AttributeType': 'S'
            # },
            # {
            #     'AttributeName': 'vintage',
            #     'AttributeType': 'N'
            # },
            # {
            #     'AttributeName': 'geography_link',
            #     'AttributeType': 'S'
            # },
            # {
            #     'AttributeName': 'variables_link',
            #     'AttributeType': 'S'
            # },
            # {
            #     'AttributeName': 'groups_link',
            #     'AttributeType': 'S'
            # },
            # {
            #     'AttributeName': 'source_path',
            #     'AttributeType': 'SS'
            # },
        ],

        # Keeps us free-tier eligible
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    ))

    # Wait for table to be created
    # table.meta.client.get_waiter('table_exists').wait(TableName=tableName)

def create():
    create_census_datasets_table()

if __name__ == '__main__':
    create()
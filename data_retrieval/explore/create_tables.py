
from boto3_wrapper.dynamodb import create_table

# DynamoDB Data Types: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.DataTypes.html

def create_data_sources_table():
    tableName = 'data_sources'
    table = create_table(dict(
        TableName=tableName,
        KeySchema=[
            {
                'AttributeName': 'name',
                'KeyType': 'HASH' # aka: the partition key (like primary key, but for NoSQL)
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
            # Columns that exist, but don't get defined in the schema:
            # {
            #     'AttributeName': 'description',
            #     'AttributeType': 'S'
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
    create_data_sources_table()

if __name__ == '__main__':
    create()
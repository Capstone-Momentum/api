
from boto3_wrapper.dynamodb import get_table
from boto3.dynamodb.conditions import Key, Attr
from constants.census.constants import ACSTableItem

def get_item(tableName, variableName, year):
    table = get_table(tableName)
    response = table.query(
        KeyConditionExpression=Key(ACSTableItem.VARIABLE_NAME.value).eq(variableName) & Key(ACSTableItem.YEAR.value).eq(year)
    )
    try:
        return response['Items'][0]
    except:
        return None


if __name__ == '__main__':
    print(get_item('census_acs1_detailed', 'B19037E_030E', 2018))


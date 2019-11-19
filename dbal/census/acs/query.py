
import boto3
from boto3.dynamodb.conditions import Key, Attr

def get_item(tableName, variable):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tableName)
    pass



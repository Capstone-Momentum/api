
import boto3

def create_table(args):
    dynamodb = boto3.resource('dynamodb')
    dynamodb.create_table(**args)

def get_table(name):
    dynamodb = boto3.resource('dynamodb')
    dynamodb.Table(name)



import boto3
from os import environ

# the hard coding of the credentials NEEDS TO CHANGE: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html

def get_dynamodb():
    return boto3.resource(
        'dynamodb',
        # aws_access_key_id='',
        # aws_secret_access_key='',
        # region_name=''
    )

def create_table(args):
    dynamodb = get_dynamodb()
    dynamodb.create_table(**args)

def get_table(name):
    dynamodb = get_dynamodb()
    return dynamodb.Table(name)


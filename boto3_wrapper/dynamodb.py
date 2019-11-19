
import boto3
from os import environ

def get_dynamodb():
    return boto3.resource(
        'dynamodb',
        aws_access_key_id='AKIA2QNHZYF3UP4HMEXZ',
        aws_secret_access_key='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',
        region_name='us-east-2'
    )

def create_table(args):
    dynamodb = get_dynamodb()
    dynamodb.create_table(**args)

def get_table(name):
    dynamodb = get_dynamodb()
    return dynamodb.Table(name)


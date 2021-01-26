import boto3
from dotenv import load_dotenv
from os import getenv

load_dotenv()

client = boto3.resource('dynamodb',
                        aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
                        aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
                        region_name=getenv("REGION_NAME"))

table = client.Table('devops-challenge')
print(table.get_item(Key={'code_name': 'thedoctor'}))

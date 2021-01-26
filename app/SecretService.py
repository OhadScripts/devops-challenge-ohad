import boto3


class Database:
    service_name = 'dynamodb'
    db_conn = None
    secret = {}

    def __init__(self,
                 aws_access_key_id,
                 aws_secret_access_key,
                 region_name):
        self.db_conn = boto3.resource(self.service_name,
                                      aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                      region_name=region_name)
        self.secret = self.get_secret()

    def get_secret(self):
        table = self.db_conn.Table('devops-challenge')
        return table.get_item(Key={'code_name': 'thedoctor'})["Item"]

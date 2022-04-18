import boto3
from decimal import Decimal
import json


def get_table(dynamodb=None):
    print("DynamoDB: Creating table")
    dynamodb_client = boto3.client('dynamodb')
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    requests_table = dynamodb.Table("311ServiceRequests")
    table_name = '311ServiceRequests'
    existing_tables = dynamodb_client.list_tables()['TableNames']

    if table_name not in existing_tables:
        print("request table: ",requests_table)
        table = dynamodb.create_table(
        TableName='311ServiceRequests',
        KeySchema=[
            {
                'AttributeName': 'SR_NUMBER',
                'KeyType': 'HASH'  # Partition key
            },

        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'SR_NUMBER',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        return table
    else:
        return requests_table

def get_table_status(table_name):
    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

    # Print out some data about the table.
    return (table.item_count)


def put_items(table, df):
    print("DynamoDB put_items called")
    table = dynamodb.Table("311ServiceRequests")
    with table.batch_writer() as batch:
        for i, row in df.iterrows():
            if(i != 0):
                print("DynamoDB put_items: ",i)
                batch.put_item(json.loads(row.to_json(), parse_float=Decimal))

    print("DynamoDB put_items completed")

import json
import s3_access
import dynamoDB_accessor
import os

def handler(event, context):
    # TODO implement
    servicereq_df = s3_access.get_data_frame()

    #create table if it doesn't exist
    servicereq_table = dynamoDB_accessor.get_table()
    #wait for it to get created and print the number of rows in it, expected to be 0.

    #Insert dataframe rows into table
    dynamoDB_accessor.put_items(servicereq_table, servicereq_df)


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

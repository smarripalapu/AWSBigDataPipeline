import pandas as pd
import json
import io
import os
import csv
import time
import uuid
import boto3
import re
from datetime import datetime
from urllib.parse import unquote_plus
from botocore.exceptions import ClientError
from io import StringIO


print('Loading function')
# get your credentials from environment variables
s3 = boto3.client('s3', region_name="us-east-1")
output_bucket = "processeddata-group9"

def handler(event, context):
  print("Hello from AWS Lambda!")
  print(pd.show_versions(as_json=False))

  bucket = event['Records'][0]["s3"]["bucket"]["name"]
  key = event['Records'][0]["s3"]["object"]["key"]
  input_file = os.path.join(bucket, unquote_plus(key))
  print("Input file: ",input_file)

  output_file_name = (os.path.splitext(os.path.basename(input_file))[0] + "_processed.csv")
  output_file = os.path.join(output_bucket, output_file_name)
  print("Output file: ",output_file)


  csv_obj = s3.get_object(Bucket=bucket, Key=key)
  body = csv_obj['Body']
  csv_string = body.read().decode('utf-8')

  df = pd.read_csv(StringIO(csv_string))
  print("Created dataframe.")

  df.dropna(subset=['STREET_ADDRESS']) #To make sure street address is not empty. Should handle invalid values
  df['CITY'] = "Chicago"
  df['STATE'] = "Illinois"
  df['ADDRESS'] = df['STREET_ADDRESS']+","+df['CITY']+","+df['STATE']
  print("Writing csv to bucket....")

  session = boto3.Session()
  s3_res = session.resource('s3')
  csv_buffer = StringIO()
  df.to_csv(csv_buffer)
  s3_res.Object(output_bucket, output_file_name).put(Body=csv_buffer.getvalue())
  print("DONE")

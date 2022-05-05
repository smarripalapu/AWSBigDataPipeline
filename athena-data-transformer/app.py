import json
import base64
import copy

def lambda_handler(event, context):
    output = []
    print('Lambda Triggered')
    print(event)
    print(context)
    for record in event['records']:
        print (record)
        # Decode from base64 (Firehose records are base64 encoded)
        payload = base64.b64decode(record['data'])

        # Read json as utf-8    
        json_string = payload.decode("utf-8")

        # Add a line break (“\n”)
        output_json_with_line_break = json_string + "\n"

        # Encode the data
        encoded_bytes = base64.b64encode(bytearray(output_json_with_line_break, 'utf-8'))
        encoded_string = str(encoded_bytes, 'utf-8')

        # Create copy of the record and append to output with transformed data
        output_record = copy.deepcopy(record)
        output_record['data'] = encoded_string
        output_record['result'] = 'Ok'

        output.append(output_record)

    print('Successfully processed records {} records.'.format(len(event['records'])))

    return {'records': output}

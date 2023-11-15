import json

def lambda_handler(event, context):
    # Assuming the payload is in the 'body' of the input event
    try:
        payload = json.loads(event['body'])
    except json.JSONDecodeError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Error decoding JSON: {str(e)}')
        }

    # You can perform any processing on the payload if needed
    
    return {
        'statusCode': 200,
        'body': json.dumps(payload)
    }

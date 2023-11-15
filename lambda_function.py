import json
import requests
import os

def lambda_handler(event, context):
    # Assuming the payload is in the 'body' of the input event
    try:
        payload = json.loads(event['body'])
        issue_url = payload.get('issue', {}).get('html_url', '')
    except json.JSONDecodeError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Error decoding JSON: {str(e)}')
        }

    # Send message to Slack
    slack_url = os.environ.get('SLACK_URL', '')
    if slack_url:
        slack_payload = {'text': f'Issue Created: {issue_url}'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(slack_url, data=json.dumps(slack_payload), headers=headers)
        # Log the response (optional)
        print(response.text)
    else:
        return {
            'statusCode': 500,
            'body': json.dumps('SLACK_URL environment variable not set')
        }

    # Return issue URL in the response
    return {
        'statusCode': 200,
        'body': json.dumps({'issue_url': issue_url, 'message': 'Slack notification sent!'})
    }

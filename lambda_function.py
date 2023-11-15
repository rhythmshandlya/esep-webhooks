import json
import requests
import os

def lambda_handler(event, context):
    issue_url = event['issue']['html_url']
    
    # Create Slack payload
    payload = {'text': f'Issue Created: {issue_url}'}
    
    # Send payload to Slack
    slack_url = os.environ['SLACK_URL']
    headers = {'Content-Type': 'application/json'}
    response = requests.post(slack_url, data=json.dumps(payload), headers=headers)
    
    # Log the response (optional)
    print(response.text)
    
    return {
        'statusCode': response.status_code,
        'body': json.dumps('Slack notification sent!')
    }

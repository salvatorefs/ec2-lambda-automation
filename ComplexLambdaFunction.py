#Uses query parameters from API Gateway to filter EC2 instances based on any tag key-value pair

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Retrieve query parameters
    key = event.get('queryStringParameters', {}).get('key')
    value = event.get('queryStringParameters', {}).get('value')
    
    # Set up filters
    filters = [{'Name': 'instance-state-name', 'Values': ['running']}]
    
    # Add tag filter if key and value are provided
    if key and value:
        filters.append({'Name': f'tag:{key}', 'Values': [value]})
    
    # Describe instances with the filters
    response = ec2.describe_instances(Filters=filters)
    
    # Get the instance IDs for instances that match the filters
    instances_to_stop = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    
    # Stop the instances if any are found
    if instances_to_stop:
        ec2.stop_instances(InstanceIds=instances_to_stop)
        return {
            'statusCode': 200,
            'body': f'Stopped instances: {instances_to_stop}'
        }
    else:
        return {
            'statusCode': 200,
            'body': 'No matching instances found or instances already stopped.'
        }

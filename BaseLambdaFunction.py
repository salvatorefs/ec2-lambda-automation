import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    instances_to_stop = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    
    if instances_to_stop:
        ec2.stop_instances(InstanceIds=instances_to_stop)
        return f'Stopped instances: {instances_to_stop}'
    else:
        return 'No running instances found.'

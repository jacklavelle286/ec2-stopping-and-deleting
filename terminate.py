import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:environment', 'Values': ['dev']},
            {'Name': 'instance-state-name', 'Values': ['running', 'stopped']}
        ])
    instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    if instances:
        ec2.terminate_instances(InstanceIds=instances)
    return {'message': f'Terminated instances: {instances}'}

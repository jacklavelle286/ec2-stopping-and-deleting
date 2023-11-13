import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:environment', 'Values': ['uat']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ])
    instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    if instances:
        ec2.stop_instances(InstanceIds=instances)
    return {'message': f'Stopped instances: {instances}'}

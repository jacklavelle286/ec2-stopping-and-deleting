# EC2 Instance Stopping and Deleting Automation
# Description
This repository contains AWS CloudFormation templates and Python Lambda functions designed to automate the stopping and termination of EC2 instances based on specific schedules and tags. It includes two main functionalities:

Stopping EC2 Instances: Automatically stops EC2 instances tagged environment:uat according to a defined schedule (between 5 PM and 9 AM daily).
Terminating EC2 Instances: Automatically terminates EC2 instances tagged environment:dev at 5 PM every day.
# Prerequisites
Before you begin, ensure you have met the following requirements:

- AWS account with necessary permissions to create Lambda functions, CloudFormation stacks, IAM roles, and EventBridge rules.
- Python 3.8 or later installed for local Lambda function development.
- AWS CLI installed and configured for deploying resources.
#Installation

To install this project, follow these steps:

1. Clone the repository to your local machine:

`git clone https://github.com/jacklavelle286/ec2-stopping-and-deleting.git`

2. Navigate to the cloned repository:

`cd ec2-stopping-and-deleting`

3. Zip the Python Lambda function files:

`zip -r stop_ec2_instances.zip stop_ec2_instances.py; zip -r terminate_ec2_instances.zip terminate_ec2_instances.py`

4. Upload the zipped Lambda function files to your S3 bucket:

`aws s3 cp stop_ec2_instances.zip s3://your-s3-bucket-name/path/`

`aws s3 cp terminate_ec2_instances.zip s3://your-s3-bucket-name/path/`

# Usage

To use this project, follow these steps:

1. Update the CloudFormation templates (stop_instances_template.yaml and terminate_instances_template.yaml) with your S3 bucket name and the path to the zipped Lambda function files.

2. Deploy the CloudFormation stacks:

`aws cloudformation create-stack --stack-name StopEC2InstancesStack --template-body file://stop_instances_template.yaml --capabilities CAPABILITY_NAMED_IAM`


`aws cloudformation create-stack --stack-name TerminateEC2InstancesStack --template-body file://terminate_instances_template.yaml --capabilities CAPABILITY_NAMED_IAM`


3. Verify the deployment in the AWS CloudFormation console and check the Lambda and EventBridge rules for correct configuration.

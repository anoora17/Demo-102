import os
import boto3

#Lambda function to create ec2 instamces from an image

# OS env values can be added
AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']


ec2 = boto3.resource('ec2')


def lambda_handler(event, context):




    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1,
        Monitoring={
        'Enabled': True
        },
        BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdh',
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 10,
                'VolumeType': 'gp2',
                'Encrypted': False
            },
        },
    ],

    )




    print("My new instance is created:", instance[0].id)
#ref https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance

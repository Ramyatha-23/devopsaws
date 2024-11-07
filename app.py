import boto3
client = boto3.client('rds')
response = client.run_instances(
    ImageId='ami-06b21ccaeff8cd686',
    InstanceType='t2.medium',
    KeyName='devprod',
    MaxCount=1,
    MinCount=2
)

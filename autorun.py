import json
import boto3
ec2 = boto3.client('ec2', 'ap-northeast-2')

def lambda_handler(event, context):
    reservations = ec2.describe_instances()
    ec2_list = []
    for attr in reservations["Reservations"]:
       for instance in attr["Instances"]:
           for tag in instance["Tags"]:
                if tag["Key"] == "AUTOSTATE" and tag["Value"] == "Yes" :
                    ec2_list.append(instance)

     


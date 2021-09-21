import json
import boto3
ec2 = boto3.client('ec2', 'ap-northeast-2')

def lambda_handler(event, context):
    reservations = ec2.describe_instances()
    ec2_list = []
    ec2_list_start = []
    ec2_list_stop = []
    for attr in reservations["Reservations"]:
       for instance in attr["Instances"]:
           for tag in instance["Tags"]:
                if tag["Key"] == "AUTOSTATE" and tag["Value"] == "Yes" :
                    ec2_list.append(instance)

     
    for tagInstance in ec2_list:
        if tagInstance["State"]["Name"] == 'running':
            ec2_list_start.append(tagInstance["InstanceId"])
            ec2.stop_instances(InstanceIds=ec2_list_start)
        elif tagInstance["State"]["Name"] == 'stopped':
            ec2_list_stop.append(tagInstance["InstanceId"])
            ec2.start_instances(InstanceIds=ec2_list_stop)
        else:
            print("Nothing to see here")


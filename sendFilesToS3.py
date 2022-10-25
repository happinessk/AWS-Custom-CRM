import time
import json
import boto3

INSTANCE_ID = 'place instance id here'

def lambda_handler(event, context):
    ssm = boto3.client('ssm')

    response = ssm.send_command(
        InstanceIds=[INSTANCE_ID],
        DocumentName="AWS-RunShellScript",
        Parameters={'commands': ['bash /home/ec2-user/transfer_files.sh']}
    )
    
    return {

        'statusCode': 200,

        'body': json.dumps('success')

    }

sendFilesToS3

import time

import json

import boto3





def lambda_handler(event, context):

    ssm = boto3.client('ssm')



    response = ssm.send_command(

        InstanceIds=['instance-id'],

        DocumentName="AWS-RunShellScript",

        Parameters={'commands': ['bash /home/ec2-user/transfer_files.sh']}

    )

sendEmails

import boto3

import json

from botocore.exceptions import ClientError





SENDER = "msiebenaler@brandeis.edu"

CONFIGURATION_SET = "ConfigSet"

AWS_REGION = "us-east-1"

SUBJECT = "RSEG176 - Group C - Email"

BODY_TEXT = ("Here is additional information!\r\n"

             "This email was sent with Amazon SES using the AWS SDK for Python (Boto)."

            )

            



BODY_HTML = """<html>

Here is additional information!

<br>

This email was sent with Amazon SES using the AWS SDK for Python (Boto)

</html>

            """            

CHARSET = "UTF-8"



def send_email(recipient):

    

    client = boto3.client('ses',region_name=AWS_REGION)

    

    try:

        response = client.send_email(

        Destination={

            'ToAddresses': [

                recipient

            ],

        },

        Message={

            'Body': {

                'Html': {

                    'Charset': CHARSET,

                    'Data': BODY_HTML

                },

                'Text': {

                    'Charset': CHARSET,

                    'Data': BODY_TEXT

                },

            },

            'Subject': {

                'Charset': CHARSET,

                'Data': SUBJECT

            },

        },

        Source=SENDER

        )



    except ClientError as e:

        print(e.response['Error']['Message'])

        

def get_recipients():

    

    s3_client = boto3.client('s3')

    bucket = 'rseg176'

    csv_file = 'emails.csv'

    csv_file_obj = s3_client.get_object(Bucket=bucket, Key=csv_file)

    recipients = csv_file_obj['Body'].read().decode('utf-8').split()

    

    return recipients



def lambda_handler(event, context):

    

    # get file contents

    

    recipients = get_recipients()

    

    # send email

    

    for recipient in recipients:

        send_email(recipient)

        

    

    # TODO implement

    return {

        'statusCode': 200,

        'body': json.dumps('Hello from Lambda!')

    }

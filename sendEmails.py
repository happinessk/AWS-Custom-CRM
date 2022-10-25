import boto3
import json
from botocore.exceptions import ClientError

#This thread was helpful: https://stackoverflow.com/questions/70286801/how-to-load-csv-files-data-from-s3-to-mysql-rds-using-lambda

SENDER = "sender email here"
CONFIGURATION_SET = "ConfigSet"
AWS_REGION = "us-east-1"
SUBJECT = "RSEG176 - Group C - Email - Event Info!"
BODY_TEXT = ("Here is additional information on upcoming events!\r\n"
             "This email was sent with Amazon SES using the AWS SDK for Python (Boto)."
            )
            

BODY_HTML = """<html>
Here is additional information on upcoming events!
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
        'body': json.dumps('success')
    }

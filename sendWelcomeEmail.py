import json
import pymysql
import rds_config
import boto3
from botocore.exceptions import ClientError

#This thread was helpful: https://stackoverflow.com/questions/70286801/how-to-load-csv-files-data-from-s3-to-mysql-rds-using-lambda
SENDER = ""
CONFIGURATION_SET = "ConfigSet"
AWS_REGION = "us-east-1"
SUBJECT = "RSEG176 - Group C - Welcome Email!"
BODY_TEXT = ("Welcome to our email program!\r\n"
             "Please go to this site to unsubscribe:\r\n"
             ""
            )



# source:
# https://levelup.gitconnected.com/aws-lambda-with-rds-using-pymysql-23ad3cde46c8
rds_host = rds_config.db_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name
port = 3306
conn = pymysql.connect(host=rds_host,user=name,
                           passwd=password,db=db_name,
                           connect_timeout=5,
                           cursorclass=pymysql.cursors.DictCursor)



BODY_HTML = """<html>
Welcome to our email program!
<br>
<br>
To unsubscribe, please click <a href="http://rseg176assignment2-env-3.eba-gm8rupye.us-east-1.elasticbeanstalk.com/">here</a>.

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

def lambda_handler(event, context):
 
  
    
    with conn.cursor() as cur:
        qry = "select distinct email_address from emails where welcome_received = 0"
        cur.execute(qry)
        rows = cur.fetchall()
        emails = []
        
        for row in rows:
            emails.append(row['email_address'])

            
    # send email
    
    for email in emails:

        send_email(email)  
        
    # update that welcome received
    
    with conn.cursor() as cur:
        for email in emails:
            qry = "update emails set welcome_received = 1 where email_address = %s"
            cur.execute(qry,(email,))
            conn.commit()

            
    return {
        'statusCode': 200
    }


## About 
This cloud service allows event coordinators to gather emails at events and upload them to a WordPress web application. On a daily basis, the emails will be pulled from WordPress and sent to the recipients with more details about the event and future events.This new service allows for distributed email uploading (web app), standardized emailing (templates), and timely emailing (scheduled).

### AWS Blueprint 📍
- miro: https://miro.com/app/board/uXjVPKjSvVU=/


## Features Include✨
- WordPress 
  - Forminator: Wordpress form feature

Amazon Web Services
  - Create an EC2 instance with a WordPress installation
  - Create an S3 bucket
  - Install the AWS CLI on the EC2 instance
  - Create a script that pushes from the EC2 instance to the S3 bucket
  - Build two Lambda functions– one to execute the script on the EC2 instance and another to send emails
  - Create two EventBridge scheduled rules- one to trigger the Lambda function that sends the file to the S3 bucket and another to send an email from the  contents of the file in the S3 bucket
  - Create identities in SES to ensure emails can be sent / delivered
  - Create security policies that allow interaction between EC2, S3, and SES


<img width="809" alt="flowchart" src="https://github.com/happinessk/AWS-Custom-CRM/blob/main/homepage.jpg">



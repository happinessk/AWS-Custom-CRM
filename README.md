## Previous goal
In our initial pilot, we provided marketers the ability to gather their own leads (consumer email addresses) and upload those leads to a self-serve website. This moved away from the old system that required marketers to login at work and send emails out from their workstations. The new system was built out in AWS utilizing EC2, S3, Lambda, EventBridge, and SES.
What we learned
Marketers were able to spend less time dealing with leads and more time finding leads. That said, the turnaround time for consumers receiving their first email was not ideal. The very important first contact hinged on how quickly a marketer uploaded their list of leads after events. Additionally, the inability to unsubscribe caused some complaints from various consumers.

## How we improved upon it
We decided to put the subscriptions back in the hands of the actual consumers. Rather than requiring marketers to subscribe to our email program, we created a web application that interested consumers can visit after seeing one of our flyers, brochures, or banners. This signup form also grants consumers the ability to unsubscribe from our email program as well.
We also included error messaging to help guide our users. We hope to further improve on error messages in the future by providing specific error messages based on the user’s situation. Currently when an error is made the user receives the following “Enter a valid email address” - in the future we hope to add the following: user forgets to add the “@” and “.” characters we will include a message stating “an email must contain a single @”, if the user leaves the field blank, the user will receive the following message, “please enter a valid email address.” 
With this increased chance of high-volume consumer signups, we would also expect more traffic to our web application as well as require an enhanced ability to monitor and clean our sensitive data (emails are PII).
We hope to review and apply design patterns techniques to help guide our work. Due to an increased chance of high-volume, we will hope to use Data Sharding as a technique to help with data storage and application performance. 

## Features we used
From a technical perspective, we decided to use ElasticBeanstalk for monitoring and load balancing our web application. And instead of a local database on an EC2 instance, we opted for RDS (with MySQL) in order to have more control on database backups with a more transparent way to access and monitor the data via external database tools. We originally used S3 to store the email addresses, and this worked well since we could access S3 without a Virtual Private Cloud. However, for the read / write operations we would need to undertake with a proper CRM, a relational database made more sense. Developers in the organization are familiar with it and PHP Laravel is designed to work well with MySQL.
With a single-page web application built in PHP Laravel, we enable the consumer to simply subscribe or unsubscribe from our email program.

## Testing
To confirm the functionality and business requirements, we performed user acceptance testing and smoke testing. In the future, we will do performance testing to find out how the application handles a significant volume of data entered combined with heavy traffic because there will be a lot of questions on the website. Additionally, we intend to run integration tests to confirm that various functionalities function well together.
Why invest in the cloud
Your company will be able to gather, store, share, and access data more simply thanks to cloud computing. Data that is saved in the cloud isn't kept on your computer's hard drive; rather, it is instead kept on internet servers that you may access from any location with just a few mouse clicks. While automating your organization's procedures, our suggested cloud application will make it simpler than ever for teams to collaborate effectively. You'll be able to work more quickly and easily because this will reduce the requirement for manual operations.

## Flow
https://github.com/happinessk/AWS-Custom-CRM/blob/assignment-2/high-level%20flow.png?raw=true![image](https://user-images.githubusercontent.com/20544603/203457867-dcba41c9-253c-4436-994a-25e6025b62ff.png)

View all the flows: https://miro.com/app/board/uXjVPKjSvVU=/

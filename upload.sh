#!/bin/sh
#store in /home/ec2-user
aws s3 rm s3://rseg176 --recursive

aws s3 sync /var/www/html/wordpress/wp-content/uploads/2022/10/ s3://rseg176 --exclude='*' --include='emails.csv'

#!/bin/sh
find /home/ec2-user/file_to_send -name "*.csv" -type f -delete
find /home/ec2-user/emails -name "*.csv" -type f -delete
find /var/www/html/wordpress/wp-content/uploads/ -name 'emails*.csv' -exec cp -pr '{}' '/home/ec2-user/emails' ';'
find /home/ec2-user/emails -type f -printf '%T@\t%p\n' | sort -t $'\t' -g | head -n -1 | cut -d $'\t' -f 2- | xargs rm
mv /home/ec2-user/emails/*.* /home/ec2-user/emails/emails.csv
cp /home/ec2-user/emails/emails.csv /home/ec2-user/file_to_send
aws s3 rm s3://rseg176 --recursive
aws s3 sync /home/ec2-user/file_to_send/ s3://rseg176
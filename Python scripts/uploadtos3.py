import boto3
import logging

filename = raw_input( "provide complete path of the file to upload....  " )
print filename
s3 = boto3.resource('s3')
data = open(filename , 'rb')
s3.Bucket('xxx-bucketname-xxx').put_object(Key='sample.txt', Body=data)
print "succcesfully uploaded the file"

import json
import boto3
#from boto3.session import Session
import requests
#import datatime

region = 'ap-northeast-1'

def lambda_handler(event, context):

    bucketList=[]
    bucketSum = 0
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('something-bucket-name')
    for object in bucket.objects.all():
        bucketSum += object.size
        #print(object.size)

    print(bucketSum)z

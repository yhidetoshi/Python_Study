import json
import boto3
#from boto3.session import Session
import requests
#import datatime

region = 'ap-northeast-1'

def lambda_handler(event, context):

    bucketList=[]
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

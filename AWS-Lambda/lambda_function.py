import json
import boto3
#from boto3.session import Session
import requests
#import datatime

region = 'ap-northeast-1'
SLACL_POST_URL = "https://hooks.slack.com/XXXXXXXXXXX"

def lambda_handler(event, context):

    bucketList=[]
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        bucketList.append(bucket.name)
        print(bucket.name)

    payload_dic = {
    "text": "s3 bucketList 200 OK",
    "icon": ':bow:',
    "channel": 'infra_as_code',
    }
    r = requests.post(SLACL_POST_URL, data=json.dumps(payload_dic))

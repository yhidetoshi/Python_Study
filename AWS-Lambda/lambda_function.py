import boto3

def lambda_handler(event, context):

    ec2 = boto3.client('ec2')
    # Check for EC2(Running)
    ec2_response = ec2.describe_instances(Filters=[{'Name':'instance-state-name','Values':['running']}] )
    ec2_count = len(ec2_response['Reservations'])
    print(ec2_count)

"""
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(id='i-019a20d3c1aa2b6a6')
    print(instance)
    name_tag = [x['Value'] for x in instance.tags if x['Key'] == 'Name']


    name = name_tag[0] if len(name_tag) else ''
    #print(name)
"""

import boto3

def lambda_handler(event, context):

    ec2 = boto3.client('ec2')
    messages_running=[]
    ec2_running_response = ec2.describe_instances(Filters=[{'Name':'instance-state-name','Values':['running']}] )
    #print(ec2_response)

    ec2_running_count = len(ec2_running_response['Reservations'])
    print(ec2_running_count)

    if ec2_running_count > 0:
        messages_running.append("EC2 Running !!")
        for i in range(0, ec2_running_count):
            running_instance = ec2_running_response['Reservations'][i]['Instances'][0]['Tags'][0]['Value']
            #print(running_instance)
            messages_running.insert(1, running_instance)
            messages_running.append(' ')
        print(messages_running)

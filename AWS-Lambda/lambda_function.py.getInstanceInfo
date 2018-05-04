import boto3

def lambda_handler(event, context):

    ec2 = boto3.client('ec2')
    running_instance_info=[]
    all_instance_info=[]

#   ec2_running_response = ec2.describe_instances(Filters=[{'Name':'instance-state-name','Values':['running']}] )
    ec2_all_response = ec2.describe_instances()
    ec2_all_count = len(ec2_all_response['Reservations'])


    # インスタンスの情報を取得(とりあえず配列に格納)
    if ec2_all_count > 0:
        summary_instance_info=[]
        for i in range(0, ec2_all_count):
            all_instance_info.append(ec2_all_response['Reservations'][i]['Instances'][0]['Tags'][0]['Value'])
            all_instance_info.append(ec2_all_response['Reservations'][i]['Instances'][0]['State']['Name'])
            all_instance_info.append(ec2_all_response['Reservations'][i]['Instances'][0]['InstanceId'])
            all_instance_info.append(ec2_all_response['Reservations'][i]['Instances'][0]['InstanceType'])
            all_instance_info.append(ec2_all_response['Reservations'][i]['Instances'][0]['PrivateIpAddress'])
            summary_instance_info = all_instance_info
            if i == 0:
                    print(summary_instance_info)
            else:
                    print(summary_instance_info[1:])
            all_instance_info = ['']

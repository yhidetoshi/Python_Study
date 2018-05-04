import boto3

region = 'ap-northeast-1'
instance = ['instance_id']

def lambda_handler(event, context):

    all_ami_info=[]
    sorted_ami=[]
    ec2_ami = boto3.client('ec2')
    images = ec2_ami.describe_images(Owners=["self"])["Images"]

    #for i in range(0, len(images)):
#        all_ami_info.append(images[i]['Name'])
#        all_ami_info.append(images[i]['CreationDate'])

    #print(all_ami_info)
    # 結果出力
    for ami in sorted(images, key = lambda x:x['CreationDate']):
        sorted_ami.append(ami)

    for i in range(0, len(sorted_ami)):
        #all_ami_info.append(sorted_ami[i]['CreationDate'])
        all_ami_info.append(sorted_ami[i]['Name'])

    print(all_ami_info)

    # 結果出力
    for j in range(0, len(all_ami_info)):
        print(all_ami_info[j])

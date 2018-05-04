## boto3の公式ドキュメントのメモ

#### create_image(**kwargs)の場合

↓ boto3の公式ドキュメントだが、 Required パラメータは `AWS API Documentation`のリンクを踏んで確認する必要がある,,,
- Request Parametersは `Request Syntax` の下に記載されている

```
Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is either running or stopped.

If you customized your instance with instance store volumes or EBS volumes in addition to the root device volume, the new AMI contains block device mapping information for those volumes. When you launch an instance from this new AMI, the instance automatically launches with those additional volumes.

For more information, see Creating Amazon EBS-Backed Linux AMIs in the Amazon Elastic Compute Cloud User Guide .

See also: AWS API Documentation

Request Syntax

response = client.create_image(
    BlockDeviceMappings=[
        {
            'DeviceName': 'string',
            'VirtualName': 'string',
            'Ebs': {
                'Encrypted': True|False,
                'DeleteOnTermination': True|False,
                'Iops': 123,
                'KmsKeyId': 'string',
                'SnapshotId': 'string',
                'VolumeSize': 123,
                'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1'
            },
            'NoDevice': 'string'
        },
    ],
    Description='string',
    DryRun=True|False,
    InstanceId='string',
    Name='string',
    NoReboot=True|False
)
```

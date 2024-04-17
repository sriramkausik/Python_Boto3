import boto3
def EBSTypeFetch():
    client = boto3.client('ec2')
    response = client.describe_volumes(        
    )
    

    print("Scanning for EBS GP2 volume")
    for volume in response['Volumes']:        
       for volumeid in volume['Attachments']:
           if 'gp2' in volume['VolumeType']:
                print("GP2 volumeid is" + " " + volumeid['VolumeId'])
EBSTypeFetch()
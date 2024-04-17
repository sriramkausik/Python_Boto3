#This module runs against AWS infra and return all the EBS GP2 volumes.
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

#=============Sample Output=====================
# Scanning for EBS GP2 volume
# GP2 volumeid is vol-013ac958bf7277a6f
# GP2 volumeid is vol-01fed90a7b111ad51
# GP2 volumeid is vol-054d7d009d9a1affd
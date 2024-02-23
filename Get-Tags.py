import boto3
def terminateEC2withEBS():
    print("This function will terminate EC2 instances running with EBS volume")
    client = boto3.client('ec2')
    response = client.describe_instances(
    Filters=[

        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        }

          
     ],
         InstanceIds=[
        'i-08be3ede7693d334d','i-0c03665bd9f906cab'
    ],
    )

    active_instance_ids = set()
    for instance in response['Reservations']:
        for ins in instance['Instances']:
            for inst in ins['Tags']:
                active_instance_ids.add(inst['Key'])
    print(active_instance_ids)
        #id= instance.id
        #print("Hi I'm inside for loop fetching the running instances")
        #instanceid=instance.block-device-mapping.volume-id
        #print('id')
    
terminateEC2withEBS()
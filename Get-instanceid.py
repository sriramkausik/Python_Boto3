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

          
     ]
    )

    active_instance_ids = set()
    for instance in response['Reservations']:
        for ins in instance['Instances']:
            active_instance_ids.add(ins['InstanceId'])
    print(active_instance_ids)
        
    
terminateEC2withEBS()
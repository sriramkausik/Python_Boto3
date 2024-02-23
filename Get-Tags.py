import boto3
def GetTags():
    #"This function will get the tags for the all the instances (Status Running) in AWS and also uses try except block to handle exceptions incase if an instance is not having a tag"
   #Refernece used : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html
    print("============================================================================")
    print ('Fetching the Ec2 instance information from AWS console')
    print("============================================================================")
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
        
    )
    #print(response)
    active_instance_ids = ['====INSTANCE ID====='] #List for storing the instance IDs 
    Tagsassociated = ['=====TAGS====='] # List for storing the tags
    for res in response['Reservations']: #Refer Request Syntax from the above given URL and traverse until it finds an instance id using recurse for loop. 
        for instance in res['Instances']:
            active_instance_ids.append(instance['InstanceId'])
    

    for res in response['Reservations']: #Refer Request Syntax from the above given URL and traverse until it finds an Tag key using recurse for loop. 
        for instance in res['Instances']:
            try: 
                for insid in instance['Tags']:
                    Tagsassociated.append(insid['Key'])
            except KeyError: #Handling an error incase if an EC2 instance doesn't have any Tags.
                Tagsassociated.append('No Keys found')

    count = len(active_instance_ids)
    #print(count)
    print("============================================================================")
    for i in range(count):
        
        print(active_instance_ids[i] + " " + " "  + " " + Tagsassociated[i] )
    print("============================================================================")

GetTags()
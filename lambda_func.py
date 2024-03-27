import boto3

def lambda_handler(event, context):
    ec2=boto3.client("ec2")
    
    # get all EBS snapshots
    response=ec2.describe_snapshots(OwnerIds=['self'])
    
    # get all active instances
    instances_response=ec2.describe_instances(Filters=[{'Name':'instance-state-name','Values':['running']}])
    active_instances_id=set()
    
    # get the instance id of active instances
    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instances_id.add(instance['InstanceId'])
            
    # get the volume id and snapshotid of each snapshots
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')
    
    # Iterate through each snapshot and delete if it's not attached to any volume or the volume is not attached to a running instance
    if not volume_id:
        ec2.delete_snapshot(SnapshotId=snapshot_id)
        print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
    else:
        # Check if the volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")

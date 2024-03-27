# AWS_project
##AWS Cloud Cost Optimization - Identifying Stale Resources
###Identifying Stale EBS Snapshots
A Lambda function is created that identifies EBS snapshots that are no longer associated with any active EC2 instance and deletes them to save on storage costs.

Description:
The Lambda function fetches all EBS snapshots owned by the same account ('self') and also retrieves a list of active EC2 instances (running and stopped). For each snapshot, it checks if the associated volume (if exists) is not associated with any active instance. If it finds a stale snapshot, it deletes it, effectively optimizing storage costs.

Procedure:
1.Create an instance
![image](https://github.com/AthullyaR/AWS_project/assets/78737460/b67b4b11-a066-4d37-8390-4650918a30af)
2.Create snapshot
![image](https://github.com/AthullyaR/AWS_project/assets/78737460/72f91975-e77e-49f4-ab13-92d71ae29002)
3.Create a lambda function
![image](https://github.com/AthullyaR/AWS_project/assets/78737460/ef4a58e1-718d-4397-8cc2-4f54b8da45d7)
4.Create policy
![image](https://github.com/AthullyaR/AWS_project/assets/78737460/7e220c5d-0f3d-4109-aeb6-7250d9d78edd)
5.Increse exec time
![image](https://github.com/AthullyaR/AWS_project/assets/78737460/99136e4f-6c47-4309-9de9-f79fab5707b5)
6.when no stale resources
![image](https://github.com/AthullyaR/AWS_project/assets/78737460/4a42adfa-f96f-48c8-b9fc-c4369bf0545e)
7.when no volume exists
![image](https://github.com/AthullyaR/AWS_project/assets/78737460/2f65e20e-946e-414a-8033-a2426ca9f358)
8.volume was not attached to any instance
![image](https://github.com/AthullyaR/AWS_project/assets/78737460/c47d0ed7-f5a9-42ca-99bc-4a3ffca683dd)
9.use cloudwatch to schedule the process
![image](https://github.com/AthullyaR/AWS_project/assets/78737460/8ded900b-6059-4423-bedc-7e8e2b8db4b0)
10.Specify the schedule
![image](https://github.com/AthullyaR/AWS_project/assets/78737460/7df35ce4-b764-412a-a300-0565c24a74e2)
11.Select the target
![image](https://github.com/AthullyaR/AWS_project/assets/78737460/efe78d6c-6e0d-4911-a8d5-7c431563c85a)










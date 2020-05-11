import boto3


def change_status(region, status, task):
    Id = input("input instance id, example - 'i-0c1082d2f1df45b10' ")
    try:
        client = boto3.client('ec2', region_name=region)
        if status == "terminated":
            print("Cant do much with terminated instance")
        elif status == "stopped" and task == "start":
            start = client.start_instances(InstanceIds=[Id], DryRun=False)
        elif status == "stopped" and task == "terminate":
            terminate = client.terminate_instances(InstanceIds=[Id], DryRun=False)
        elif status == "stopped" and task == "stop":
            print("Already stopped")
        elif status == "started" and task == "stop":
            stop = client.stop_instances(InstanceIds=[Id], DryRun=False)
        elif status == "started" and task == "terminate":
            terminate = client.terminate_instances(InstanceIds=[Id], DryRun=False)
        elif status == "started" and task == "start":
            print("Already started")
        elif status == "started" and task == "reboot":
            stop = client.reboot_instances(InstanceIds=[Id], DryRun=False)
        elif status == "stopped" and task == "reboot":
            print("Cant reboot stopped instance")
    except Exception:
        print("something's wrong, please check input values")
        print("expected action parameters: start, stop, reboot, terminate")
        print("expected status parameters: started, stopped, terminated")

#    stop_hibernate = client.hibernate_instances(InstanceIds=[Id], DryRun=False) cant use because of free tier of EC2

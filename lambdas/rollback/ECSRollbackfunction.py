import boto3
import json
import s3



ecs = boto3.client('ecs', region_name='us-east-2')

def lambda_handler(event, context):
    x = event['service_name']
    y = x[8:]
    service_name = y
    cluster_name = event['cluster_name']

    _services = ecs.describe_services(cluster=cluster_name, services=[service_name])
    task_definition = _services['services'][0][u'taskDefinition']
    previous_task_definition = get_previous_task_definition(task_definition)

    ecs.update_service(cluster=cluster_name, service=service_name, taskDefinition=previous_task_definition)
    print("Rollback Complete")
    return {"Rollback": True, "service_name": service_name, "cluster_name": cluster_name}

def get_previous_task_definition(task_definition):
    previous_version_number = str(int(task_definition.split(':')[-1])-1)
    previous_task_definition = ':'.join(task_definition.split(':')[:-1]) + ':' + previous_version_number
    return previous_task_definition


get_previous_task_definition
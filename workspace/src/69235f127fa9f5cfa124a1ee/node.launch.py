import json
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    parameters = json.loads('{"joint_ids":["69235f017fa9f5cfa124a1d8"],"control_mode":"velocity","max_velocity":4}')
    configuration = json.loads('{"namespace":"/robot/base","rate_hz":150,"lifecycle":true}')
    inbound_connections = json.loads('[]')
    outbound_connections = json.loads('[]')
    env = {
        "POLYFLOW_NODE_ID": "69235f127fa9f5cfa124a1ee",
        "POLYFLOW_PARAMETERS": json.dumps(parameters),
        "POLYFLOW_CONFIGURATION": json.dumps(configuration),
        "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(inbound_connections),
        "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(outbound_connections),
    }

    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["python3", "workspace/src/69235f127fa9f5cfa124a1ee/odrive-s1/node.py"],
                additional_env=env,
                output="screen",
            )
        ]
    )
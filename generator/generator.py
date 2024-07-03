sample_data = [
    {
        "stateMachineArn": "StateMachine1",
        "executionArn": "execution1",
        "status": "RUNNING",
        "input": {"EventName": "eventA"}
    },
    {
        "stateMachineArn": "StateMachine1",
        "executionArn": "execution2",
        "status": "RUNNING",
        "input": {"EventName": "eventB"}
    },
    {
        "stateMachineArn": "StateMachine1",
        "executionArn": "execution3",
        "status": "RUNNING",
        "input": {"EventName": "eventA"}
    },
]

from typing import Iterator

def iter_execution(status = "RUNNING") -> Iterator[dict]:
  for execution in sample_data:
    if execution["status"] == status:
      yield execution

def stop_ecs_execution(event_name: str = None):
  for execution in filter(lambda x: x["input"]["EventName"] == event_name, iter_execution()):
    execution["status"] = "STOP"
    print(f"Stop the execution {execution}")

stop_ecs_execution("eventA")

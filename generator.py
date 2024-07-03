# Problem 8 - generator
# Write some examples using python generator here.

"""
Case: Find each execution in ECS's statemachine1 and stop the ones with eventA
"""

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

# Explain the benefit of generators here.
# 1. Save Memory: Avoid loading all executions into memory at once.
# 2. Good to Reuse and East Testing
# 3. Lazy Evaluation: Specific execution only computed when needed.
# 4. Easy to Extend and Read: Easily add more conditions in iterator.
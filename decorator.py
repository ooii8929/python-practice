# Problem 7 - decorator
# Write some examples using python decorator here.

"""
Case: Simulate how to use decorators to reduce code duplication and enhance flexibility, using a built-in decorator and a custom log_decorator to improve the DB model as example.
"""

def log_decorator(func):
  def wrapper(*args):
    print(f"Logging: update desired count")
    return func(*args)
  return wrapper

class ECS():
  def __init__(self):
    self.desired_count = 1

  @property
  def desired_count(self) -> int:
    return self.desired_count

  @desired_count.setter
  @log_decorator
  def desired_count(self, value: int):
    print(f"update desired count to {value}")

ecs = ECS()
ecs.desired_count = 5
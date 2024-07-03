# Problem 4 - *args, **kwargs
# Write some examples with *args, **kwargs here.

"""
Case: Simulate how to use *args and **kwargs, using handling streaming service events as an example.
"""

class Event:
  def __init__(self, Name: str = None, *args, **kwargs):
    self.Name = Name
    self.Type = list(args)
    self.ExtraInfo = kwargs

  def display_info(self):
    type_str = ", ".join(self.Type)
    print(f"EventName is {self.Name}, Type is {type_str}")

class Vod(Event):
  def __init__(self, Rate: str = None, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.Rate = Rate

  def display_info(self):
    super().display_info()
    print(f"Rate is {self.Rate}")



vod = Vod("G", "test", "Love" , "Horror")
vod.display_info()


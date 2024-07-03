class Event:
  def __init__(self, Name: str = None):
    self.Name = Name

  def display_info(self):
    print(f"EventName is {self.Name}")

class Vod(Event):
  def __init__(self, Rate: str = None, **kwargs):
    super().__init__(**kwargs)
    self.Rate = Rate

  def display_info(self):
    super().display_info()
    print(f"Rate is {self.Rate}")

vod = Vod(Name = "test", Rate = "G")
vod.display_info()
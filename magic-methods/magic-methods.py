events = [
    {
        "EventName": "vod-a",
        "duration":10
    },
     {
        "EventName": "vod-b",
        "duration":4
    },
     {
        "EventName": "live",
        "duration":20
    },
]

class Event:
  def __init__(self, Name: str = None, Duration: int = None):
    self.Name = Name
    self.Duration = Duration

  def __gt__(self,other):
    print(f"Is the duration of {self.Name} longer than the duration of {other.Name} ?")
    return self.Duration > other.Duration

event_a = Event("vod-a", 20)
event_b = Event("vod-b", 40)

print(event_a > event_b)
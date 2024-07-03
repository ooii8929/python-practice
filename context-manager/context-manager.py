input_event = {
    "EventName": "a",
}

existed_events = [
    {
        "EventName": "b"
    },
    {
        "EventName": "c"
    }
]

class DatabaseConnection:
  def __init__(self):
    self.table = existed_events

  def __enter__(self):
    print("Connect to DB")
    return self

  def __exit__(self):
    print("Disconnect to DB")
    return self

  def save_event(self, event):
    print(f"Saving {event}")
    self.table.append(event)
    return existed_events

db = DatabaseConnection()
db.save_event(input_event)
print(existed_events)
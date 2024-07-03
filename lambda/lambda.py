events = [
    {
        "EventName": "vod",
        "duration":10
    },
     {
        "EventName": "vod",
        "duration":4
    },
     {
        "EventName": "live",
        "duration":20
    },
]

filter_event_name = list(filter(lambda x:x.get("EventName","").startswith("vod"), events))

max_duration = max(filter_event_name, key= lambda x: x.get("duration", 0))
print(max_duration)

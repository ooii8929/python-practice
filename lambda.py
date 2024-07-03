
# Problem 5 - lambda
# Write some examples using python lambda here.

"""
Case: Simulate how to handle complicated data using lambda functions to keep your code clean, using finding the maximum duration within the same events as an example.
"""

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
#TODO: Add condition
max_duration = max(filter_event_name, key= lambda x: x.get("duration", 0))
print(max_duration)

events = [
    {
        "EventName": "live-b",
        "Services": [
            {"cluster": "cms", "service": "cms-api", "size": 10},
            {"cluster": "client", "service": "playback", "size": 6},
        ]
    },
     {
        "EventName": "vod-c",
        "Services": [
            {"cluster": "cms", "service": "cms-api", "size": 5},
            {"cluster": "client", "service": "web", "size": 3},
        ]
    },
    {
        "EventName": "live-a",
        "Services": [
            {"cluster": "cms", "service": "cms-api", "size": 2},
            {"cluster": "client", "service": "playback", "size": 2},
        ]
    }
]

# Comprehension - List
# Combine all service
all_services = [service for event in events for service in event["Services"]]

# Group cluster and service for size compare
grouped_service = {}
for service in all_services:
  key = (service["cluster"], service["service"])
  if key not in grouped_service:
    grouped_service[key] = []
  grouped_service[key].append(service["size"])

# Comprehension - Dict
# Get max size
max_size_service = {key: max(value) for key, value in grouped_service.items()}

print(max_size_service)


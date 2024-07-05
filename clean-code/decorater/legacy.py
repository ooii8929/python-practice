def process_data(data):
    if data <= 0:
        raise ValueError("Data must be a positive integer")
    return data * 2

def analyze_data(data):
    if data <= 0:
        raise ValueError("Data must be a positive integer")
    return data / 2

def report_data(data):
    if data <= 0:
        raise ValueError("Data must be a positive integer")
    return f"Report: {data}"
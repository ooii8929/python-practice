def positive_integer_required(func):
    def wrapper(data):
        if data <= 0:
            raise ValueError("Data must be a positive integer")
        return func(data)
    return wrapper

@positive_integer_required
def process_data(data):
    return data * 2

@positive_integer_required
def analyze_data(data):
    return data / 2

@positive_integer_required
def report_data(data):
    return f"Report: {data}"

# 測試重構後的代碼
print(process_data(10))  # 20
print(analyze_data(10))  # 5.0
print(report_data(10))   # Report: 10
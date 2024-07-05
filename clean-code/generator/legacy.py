def process_data(data):
    results = []
    for i in data:
        result = i**2
        results.append(result)
    return results

data = range(100)
results = process_data(data)
print(results[:10])
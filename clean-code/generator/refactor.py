def process_data(data):
    for i in data:
        yield i**2
    # results = []
    # for i in data:
    #     result = i**2
    #     results.append(result)
    # return results

data = range(100)
results = process_data(data)
after_result = []
for i, result in enumerate(results):
    if i < 10:
        after_result.append(result)

print(after_result)

# print(results[:10])
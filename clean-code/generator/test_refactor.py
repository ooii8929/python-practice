from refactor import process_data

def test_process_data():
    data = range(10)
    results = list(process_data(data))
    assert results == [i**2 for i in data]

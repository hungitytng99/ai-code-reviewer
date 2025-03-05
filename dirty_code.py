import json

def load_json_file(file_path):
    file = open(file_path, "r")
    data = json.load(file)
    return data

def divide_numbers(a, b):
    return a / b

def process_data():
    data = load_json_file("data.json")
    print("Processing data...")

    for item in data:
        result = divide_numbers(item["value"], item["divider"])
        print("Result:", result)

process_data()
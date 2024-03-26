import json
import threading


def parse_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        print(f"Data from {filename}: {data}")
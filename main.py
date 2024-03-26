import json
import threading


# Function to parse JSON data from a file
def parse_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        print(f"Data from {filename}: {data}")


# List of filenames containing JSON data
filenames = ["file1.json", "file2.json", "file3.json"]

# List to store thread objects
threads = []

# Loop over each filename to create a thread for parsing JSON data
for filename in filenames:
    thread = threading.Thread(target=parse_json, args=(filename,))
    threads.append(thread)
    thread.start()

# Wait for each thread to complete its task before proceeding
for thread in threads:
    thread.join()
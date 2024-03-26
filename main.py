import json
import threading
from queue import Queue
import time

# Exercise N1
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


# Exercise N2

# Function that represents a worker thread
def worker(task_queue):
    while True:
        num = task_queue.get()

        if num is None:
            break

        print(f"Thread {threading.current_thread().name} got value: {num}, is even: {num % 2 == 0}")
        time.sleep(1)
        task_queue.task_done()

# Initialize the queue
task_queue = Queue()

# Number of threads
num_threads = 3
threads = []

# Create threads
for _ in range(num_threads):
    thread = threading.Thread(target=worker, args=(task_queue,))
    thread.start()
    threads.append(thread)

# Data to be added to the queue
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Add data to the queue
for item in data:
    task_queue.put(item)

# Wait for all tasks in the queue to be processed
task_queue.join()
import threading
import queue
import time
import random


class SharedBuffer:
    def __init__(self, size):
        self.buffer = queue.Queue(size)
        self.lock = threading.Lock()


def producer(shared_buffer, data_type, total_produce):
    for _ in range(total_produce):
        item = None
        if data_type == "int":
            item = random.randint(1, 100)
        elif data_type == "float":
            item = random.uniform(1.0, 100.0)
        elif data_type == "string":
            item = f"String-{random.randint(1, 100)}"
        elif data_type == "pojo":
            item = {"key": random.randint(
                1, 100), "value": f"Value-{random.randint(1, 100)}"}

        with shared_buffer.lock:
            if not shared_buffer.buffer.full():
                shared_buffer.buffer.put(item)
                print(f"Produced {data_type}: {item}")
            else:
                print("Buffer is full. Producer is waiting.")
        time.sleep(random.uniform(0.1, 1.0))


def consumer(shared_buffer, total_consume):
    for _ in range(total_consume):
        with shared_buffer.lock:
            if not shared_buffer.buffer.empty():
                item = shared_buffer.buffer.get()
                print(f"Consumed: {item}")
            else:
                print("Buffer is empty. Consumer is waiting.")
        time.sleep(random.uniform(0.1, 1.0))


buffer_size = 5
shared_buffer = SharedBuffer(buffer_size)

total_produce = 10
total_consume = 10

producer_thread = threading.Thread(
    target=producer, args=(shared_buffer, "int", total_produce))
consumer_thread = threading.Thread(
    target=consumer, args=(shared_buffer, total_consume))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

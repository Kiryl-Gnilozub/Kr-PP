import threading
import time


def print_thread_state(thread_name, state):
    print(f"Thread {thread_name} is in {state} state.")


def thread_function(name, duration):
    print_thread_state(name, "NEW")

    time.sleep(1) 

    print_thread_state(name, "RUNNABLE")
    thread_lock.acquire() 

    print_thread_state(name, "TIMED_WAITING")
    time.sleep(duration) 

    thread_lock.release()
    print_thread_state(name, "TERMINATED")


thread_lock = threading.Lock()

thread1 = threading.Thread(target=thread_function, args=("Thread-1", 3))
thread2 = threading.Thread(target=thread_function, args=("Thread-2", 5))
thread3 = threading.Thread(target=thread_function, args=("Thread-3", 2))

print("Before starting threads:")
print_thread_state("Thread-1", "NEW")
print_thread_state("Thread-2", "NEW")
print_thread_state("Thread-3", "NEW")

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("\nAfter finishing threads:")
print_thread_state("Thread-1", "TERMINATED")
print_thread_state("Thread-2", "TERMINATED")
print_thread_state("Thread-3", "TERMINATED")

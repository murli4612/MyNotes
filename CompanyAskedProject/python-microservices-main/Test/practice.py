import threading
import time

def cpu_task():
    print("Starting task...")
    for i in range(10):
        i = i * 2  # CPU-intensive task
        print(i)
        
    print("Task completed.")

# Run two threads
start_time = time.time()
t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Time taken: {time.time() - start_time:.2f} sec")
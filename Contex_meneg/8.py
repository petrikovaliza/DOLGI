import time
import requests

class Timeout:
    def __init__(self, max_time):
        self.max_time = max_time
        self.start = None
    
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        if elapsed > self.max_time:
            raise TimeoutError(f"Execution took {elapsed:.2f} seconds, exceeded {self.max_time} seconds")


try:
    with Timeout(2):
        requests.get("https://yandex.ru", timeout=1)
        print("Request completed fast")
except TimeoutError as e:
    print(e)

try:
    with Timeout(1):
        time.sleep(2)
        print("This will not print")
except TimeoutError as e:
    print(e)

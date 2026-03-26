import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        print(f"Execution time: {self.end - self.start:.4f} seconds")


with Timer():
    time.sleep(2)
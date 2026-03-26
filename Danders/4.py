import time

class Timer:
    def __init__(self, unit='s'):
        self.unit = unit
        self.start_time = None
    
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start_time
        if self.unit == 'ms':
            elapsed *= 1000
            print(f"Execution time: {elapsed:.2f} ms")
        elif self.unit == 's':
            print(f"Execution time: {elapsed:.4f} s")
        else:
            print(f"Execution time: {elapsed:.4f} {self.unit}")


with Timer(unit='ms'):
    time.sleep(1)

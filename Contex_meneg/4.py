class Counter:
    count = 0
    
    def __enter__(self):
        Counter.count += 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Current count: {Counter.count}")


with Counter():
    print("Operation 1")

with Counter():
    print("Operation 2")

with Counter():
    print("Operation 3")
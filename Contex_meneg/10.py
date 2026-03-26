class Repeat:
    def __init__(self, times):
        self.times = times
        self.current = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def __call__(self, func):
        def wrapper():
            for i in range(self.times):
                print(f"Repeat {i+1}/{self.times}:")
                func()
                if i < self.times - 1:
                    print()
        return wrapper


with Repeat(3) as repeat:
    
    @repeat
    def test_func():
        print("  Doing something")
    
    test_func()
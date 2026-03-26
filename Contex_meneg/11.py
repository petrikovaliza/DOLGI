class IgnoreException:
    def __init__(self, *exceptions):
        self.exceptions = exceptions
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, self.exceptions):
            print(f"Ignored exception: {exc_val}")
            return True
        return False


print("Case 1 - Ignore ValueError:")
with IgnoreException(ValueError):
    x = int("not a number")
    print("This will still execute after exception")

print("\nCase 2 - Ignore ZeroDivisionError and ValueError:")
with IgnoreException(ZeroDivisionError, ValueError):
    result = 10 / 0
    print("This will still execute")

print("\nCase 3 - Exception not ignored:")
try:
    with IgnoreException(ValueError):
        result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError was not ignored, caught outside")
class SafeList:
    def __init__(self, lst):
        self.original = lst
        self.copy = None
    
    def __enter__(self):
        self.copy = self.original[:]
        return self.copy
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.original.clear()
            self.original.extend(self.copy)


my_list = [1, 2, 3, 4]
print(f"Before: {my_list}")

with SafeList(my_list) as safe:
    safe.append(5)
    safe.append(6)
    safe[0] = 100

print(f"After: {my_list}")
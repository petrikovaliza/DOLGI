class Chain:
    def __init__(self, value):
        self.value = value
    
    def __call__(self, func):
        self.value = func(self.value)
        return self
    
    def __getattr__(self, name):
        def wrapper(*args):
            if name == 'add':
                self.value = self.value + args[0]
            elif name == 'subtract':
                self.value = self.value - args[0]
            elif name == 'multiply':
                self.value = self.value * args[0]
            elif name == 'divide':
                self.value = self.value / args[0]
            return self
        return wrapper
    
    def get(self):
        return self.value


obj = Chain(5)
result = obj.add(3).multiply(2).subtract(1).get()
print(result)

obj2 = Chain(10)
result2 = obj2.multiply(2).add(5).divide(5).get()
print(result2)
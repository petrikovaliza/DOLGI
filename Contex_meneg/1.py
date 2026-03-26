class GreetingContext:
    def __enter__(self):
        print("Hello!")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Bye!")


with GreetingContext():
    print("I am inside the context")
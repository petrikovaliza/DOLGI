def say_hello(name):
    print(f"Hello, {name}!")

def say_goodbye(name):
    print(f"Goodbye, {name}!")

def say_custom(greeting):
    def inner(name):
        print(f"{greeting}, {name}!")
    return inner

def greet_user(name, callback):
    callback(name)


greet_user("Vasya", say_hello)
greet_user("Petya", say_goodbye)

custom_greet = say_custom("Good morning")
greet_user("Masha", custom_greet)
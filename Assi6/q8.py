def display_message(func):
    def wrapper():
        print("Function execution started")
        func()
        print("Function execution completed")
    return wrapper

@display_message
def greet():
    name = input("Enter name: ")
    print("Hello", name)

greet()

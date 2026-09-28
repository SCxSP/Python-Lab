def show_args(func):
    def wrapper(*args, **kwargs):
        print("Args:", args, "Kwargs:", kwargs)
        return func(*args, **kwargs)
    return wrapper

@show_args
def add(a, b):
    return a + b

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Result:", add(a, b))

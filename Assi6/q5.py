def outer(msg):
    def inner():
        print("Message:", msg)
    return inner

m = input("Enter message: ")
f = outer(m)
f()

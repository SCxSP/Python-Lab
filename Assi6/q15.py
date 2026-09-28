class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

t = input("Enter title: ")
a = input("Enter author: ")
p = float(input("Enter price: "))
b = Book(t, a, p)
b.display()

books = []
for i in range(5):
    t = input("Enter title: ")
    a = input("Enter author: ")
    p = float(input("Enter price: "))
    books.append((t, a, p))
books = tuple(books)
for b in books:
    print(b[0], b[1], b[2])

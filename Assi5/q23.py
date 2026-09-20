class CountDown:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 1:
            raise StopIteration
        val = self.num
        self.num -= 1
        return val

n = int(input("Enter start no: "))
for x in CountDown(n):
    print(x)

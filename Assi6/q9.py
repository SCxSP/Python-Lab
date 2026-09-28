import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f"Time: {t2 - t1:.6f}s")
        return res
    return wrapper

@measure_time
def compute(n):
    return sum(i * i for i in range(n))

n = int(input("Enter n: "))
print("Sum of squares:", compute(n))

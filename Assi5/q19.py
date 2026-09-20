def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input("Enter nos: ").split()))
primes = list(filter(is_prime, numbers))
print("Primes:", primes)

def isPrimary(n):
    if n == 1:
        print("1 is special.")
        return False

    for x in range(2, n):
            if n % x == 0:
                # print("{} equals {} x {}".format(n, x, n // x))
                return False
    else:
        print(n, "is a primary number.")
        return True


def primes(n=1):
    while True:
        if isPrimary(n): yield n
        n += 1


for i in primes():
    if i > 30: break

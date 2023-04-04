import multiprocessing


def print_odd_numbers():
    for i in range(100, 201):
        if i % 2 != 0:
            print("Odd number:", i)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def print_prime_numbers():
    for i in range(200, 301):
        if is_prime(i):
            print("Prime number:", i)


def is_armstrong(n):
    sum = 0
    order = len(str(n))
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if n == sum:
        return True
    return False


def generate_armstrong_numbers():
    for i in range(100, 301):
        if is_armstrong(i):
            print("Armstrong number:", i)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_odd_numbers)
    p2 = multiprocessing.Process(target=print_prime_numbers)
    p3 = multiprocessing.Process(target=generate_armstrong_numbers)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

import threading

num = 0
cond = threading.Condition()


def print_odd_numbers():
    global num
    with cond:
        while num < 10:
            while num % 2 == 0:
                cond.wait()
            print("Odd Number:", num)
            num += 1
            cond.notify()


def print_even_numbers():
    global num
    with cond:
        while num < 10:
            while num % 2 == 1:
                cond.wait()
            print("Even Number:", num)
            num += 1
            cond.notify()


t1 = threading.Thread(target=print_odd_numbers)
t2 = threading.Thread(target=print_even_numbers)

t1.start()
t2.start()

t1.join()
t2.join()

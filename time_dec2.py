import time


def time_it(f):
    def inner():
        a = time.time()
        f()
        b = time.time()
        print(b - a)

    return inner


@time_it
def cheng():
    sum = 1
    for i in range(1, 999):
        sum *= i


cheng()
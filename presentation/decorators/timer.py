import time


def make_timer(func):
    def new_func():
        start = time.time()
        print(func())
        end = time.time()
        duration = end - start 
        print(f'Function took {duration} seconds') 

    return new_func


@make_timer
def big_sum():
    s = 0
    for i in range(50000000):
        s += i
    return s


@make_timer
def very_long():
    time.sleep(2)
    return 100


big_sum()
very_long()
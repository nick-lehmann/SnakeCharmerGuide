import time

def timit(func):
    def new_function():
        start = time.time()
        print(dir(func))
        func()
        end = time.time()
        print(f"Time taken: {end - start}")
    
    return new_function


# @timit
def long_running_operation():
    s = 0
    for i in range(50000000):
        s += i
    return s


print("Running with new function")
timed_long_running_operation = timit(long_running_operation)
timed_long_running_operation()

# print("Running with decorator")
# long_running_operation()

# Decorator to log execution time of a function

import time


def log_exec_time(func):
    def wrapper():
        start = time.time_ns()
        func()
        end = time.time_ns()
        print("seconds passed %0.4f" % ((end-start)/1000000000))
    return wrapper


def do_something():
    cnt = 0
    for a in range(0, 1000000):
        cnt += a


# decorate do_something function
do_something = log_exec_time(do_something)
do_something()

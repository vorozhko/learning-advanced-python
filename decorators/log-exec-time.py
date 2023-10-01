# Decorator to log executim time of a function

import time

def log_exec_time(func):
    def wrapper():
        start = time.time_ns()
        func()
        end = time.time_ns()
        print("seconds passed %0.4f" % ((end-start)/1000000000))
    return wrapper

def do_smth():
    cnt = 0
    for a in range(0, 1000000):
        cnt += a
    

do_smth = log_exec_time(do_smth)
do_smth()

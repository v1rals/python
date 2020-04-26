#! /usr/bin/python3
import time
from functools import wraps
def delay(func):
    @wraps(func)
    def the_wrapper_around_the_original_function():
        print("начало паузы")
        time.sleep(3)
        func()  # Сама функция
        print("конец паузы")
    return the_wrapper_around_the_original_function
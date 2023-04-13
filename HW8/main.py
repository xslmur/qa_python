# 1. Напишіть декоратор, який визначає час виконання функції.
#    Заміряйте час іиконання функцій з попереднього ДЗ
# 2. Візьміть функції з попереднього ДЗ, покладіть їх у файл lib.py і імпортуйте в основний файл для виконання

import time
import lib
#from lib import (
#    get_season_name,
#    dumb_calc
#)

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret =  func(*args, **kwargs)
        diff = time.time() - start_time
        print(f"'{func.__name__}' call took: {diff:.6f} seconds")
        return ret

    return wrapper


@measure_time
def test_func():
    print('zzz...')
    time.sleep(1)
    return 42

#decorate imported functions
get_season_name = measure_time(lib.get_season_name)
dumb_calc = measure_time(lib.dumb_calc)

#test wrapper
print(test_func())

#test get_season_name call
date_str = '01.01'
print(f'get_season_name({date_str}): ', get_season_name(date_str))

#test dumb_calc call
calc_args = (8,8,'*')
print(f'dumb_calc({calc_args}): ', dumb_calc(*calc_args))

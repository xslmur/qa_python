# Напишіть функцію, яка приймає два аргументи.
# Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
# Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
# В будь-якому іншому випадку - функція повертає кортеж з двох агрументів

def is_number(a):
    if isinstance(a, bool):
        return False
    return isinstance(a, (int, float, complex))


def process_vars(a, b):
    if is_number(a) and is_number(b):
        return a * b
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    return (a, b)


test_data = [
    [3, 7],
    [3.0, 7.0],
    [complex(3.0, 0), complex(7.0, 0)],
    ['a', 'b'],
    [42, 'a'],
    [42, True]
]
for test_args in test_data:
    print(test_args,'=>',process_vars(*test_args))
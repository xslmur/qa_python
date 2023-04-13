# QA Automation Python 14.03.2023
# Karpynska Karolina
# ДЗ 8. HW7
# 1. Напишіть функцію, яка визначає сезон за датою. Функція отримує стрінг у форматі "[день].[місяць]"
#     (наприклад "12.01", "30.08", "1.11" і тд) і повинна повернути стрінг з відповідним сезоном,
#     до якого відноситься ця дата ("літо", "осінь", "зима", "весна")
# 2. Напишіть функцію "Тупий калькулятор", яка приймає два числових аргументи і строковий, який відповідає за операцію між ними (+ - / *).
# 	   Функція повинна повертати значення відповідної операції (додавання, віднімання, ділення, множення), інші операції не допускаються.
#     Якщо функція оримала невірний тип данних для операції (не числа) або неприпустимий (невідомий) тип операції
#     вона повинна повернути None і вивести повідомлення "Невірний тип даних" або "Операція не підтримується" відповідно.
# 3. Напишіть докстрінг для обох функцій


def get_season_name(date_str):
    """
    get year season by the date.
    note: no checking for the max days count in the  month

    :param date_str: date in the format "DD.MM" (e.g: "28.01")
    :type date_str: str
    :return: season description
    :rtype: str
    """
    seasons_description = ('winter','spring','summer','autumn')

    day_month_list = date_str.split('.')
    if len(day_month_list) != 2:
        raise ValueError('DD.MM expected ')

    day, month = day_month_list

    if not day.isnumeric():
        raise ValueError('day should be numeric')
    day = int(day)
    if day < 1 or day > 31:
        raise ValueError('day should be within [1-31]')

    if not month.isnumeric():
        raise ValueError('month should be numeric')
    month = int(month)
    if month < 1 or month > 12:
        raise ValueError('month should be within [1-12]')

    return seasons_description[int(month / 3) % 4]


def dumb_calc(arg1, arg2, operation):
    """

    performs the requested operation with the two args

    :param arg1: first argument for operation
    :type arg1: int | float
    :param arg2: second argument for operation
    :type arg2: int | float
    :param operation: string with the desired operation. supported operations: '+','-','/','*'
    :return: calculation result
    :rtype int | float
    """
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y,
        '*': lambda x, y: x * y,
    }

    if not all([isinstance(arg1, (int, float)),
               isinstance(arg2, (int, float)),
               isinstance(operation, str)]):
        print('Невірний тип даних')
        return None

    if operation not in operations:
        print('Операція не підтримується')
        return None

    return operations[operation](arg1, arg2)

def perform_tests():
    #get_season_name(date_str) tests
    for date in [
        #positive tests
        "01.12",
        "01.01",
        "01.02",
        "01.03",
        "01.05",
        "01.06",
        "01.08",
        "01.10",
        "01.11",
        #negative tests
        "01",
        "01.01.01",
        "qq.01",
        "99.01",
        "01.qq",
        "01.99"
    ]:
        try:
            print(date,'=>', get_season_name(date))
        except ValueError as e:
            print(date, '=> exception: ', e)

    #dumb_calc(arg1, arg2, operation) tests
    for args in [
        #positive tests
        (2,3,'+'),
        (2,3,'-'),
        (8,4,'/'),
        (8,8,'*'),
        #negative tests
        ('a', 3, '+'),
        (3, 'a', '+'),
        (1, 2, 42),
        (1, 1, '@'),
    ]:
        print('dumb_calc', args,'=>', dumb_calc(*args))

if __name__ == '__main__':
    perform_tests()
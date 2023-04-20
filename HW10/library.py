"""
Написати функцію, котра отримує стрічку та повертає цю стрічку,
проте очищену від малих літер ("длоОЛО  55 ! " має повернути "ОЛО").
окрім того довжина стрічки не має перевищувати 25 символів
(все що більше просто обрізається)

покрити тестами

перевірити flake8, mypy

не забувайте про аннотації типів і докстрінги при потребі
"""


def remove_lowercase(input_string: str) -> str:
    """
    * truncates string to the 25 characters
    * removes all NOT uppercase characters from the string

    :param input_string: string to process
    :type input_string: str
    :return: truncated and filtered string
    :rtype: str
    """
    ret = ''.join(filter(lambda c: c.isupper(), input_string))[:25]
    return ret


if __name__ == '__main__':
    print(remove_lowercase('длоОЛО  55 !'))

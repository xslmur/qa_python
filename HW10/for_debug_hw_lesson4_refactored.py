"""
симулятор каси магазину
код, наведений нижче,
приймає від покупця наступну інформацію про закупівлю 2-х товарів
- назва
- кількість (ціле число)
- ціна за одиницю
на підставі отриманих даних формується чек
всі ціни та вартість мають бути виведені в форматі з копійками,
кількість - цілі числа

програма розрахована на використання на території України
"""

import textwrap
from datetime import datetime
from decimal import Decimal


"""
refactoring notes:
    * move repeated item input to the function get_item_from_user_input()
    * collect items to the list
    * move receipt printing to the function print_receipt()
    * ljust() and textwrap.shorten() for item title
      were moved to the template processing
    * fix items total quantity value
      (sum was concatenated strings instead of the expected integer sum)
    * automatically fixed second item total cost and summary total cost
    * changed precision for Decimal: 1.0000 -> 1.00
    * use python format() width specs instead of '\t'
    * dynamically compute spacing between columns
    * swap textwrap.shorten and ljust for item title
    * fix: round price to the 0.00 precision before multiplication
"""


def get_item_from_user_input(item_counter_description: str) -> tuple:
    """
    asks user for the item name,quantity,price and returns them as a tuple

    :param item_counter_description: text with the item counter description
    :type item_counter_description: str
    :return: tuple with item's (name, quantity, price)
    :rtype tuple
    """

    item_title = input(f'Введіть назву {item_counter_description} товару: ')
    item_quantity = input(
        f'Введіть бажаєму кількість {item_counter_description} товару: '
    )
    item_price = input(f'Введіть ціну {item_counter_description} товару: ')

    return item_title, item_quantity, item_price


def get_items() -> list:
    # TODO: find the way to get descriptions from integer
    # (smth like humanfriendly)
    item_counter_descriptions = ['першого', 'другого']

    # get 2 items from user
    receipt_items = []
    for i in range(2):
        receipt_items.append(
            get_item_from_user_input(item_counter_descriptions[i]))

    return receipt_items


def quantized(val: str | Decimal) -> Decimal:
    """
    casts input string or Decimal to the Decimal with precision 0.00

    :param val: value to cast
    :return: Decimal with precision 0.00
    """
    # from: https://docs.python.org/3/library/decimal.html#decimal-faq
    two_places = Decimal(10) ** -2
    if isinstance(val, str):
        val = Decimal(val)
    return val.quantize(two_places)


def print_receipt(items: list, width: int = 80, title_width: int = 20) -> None:

    header_names = ['Товар', 'кількість', 'ціна', 'вартість']

    # compute free space between columns
    columns_free_space = width - title_width
    for hdr in header_names[1:]:
        columns_free_space -= len(hdr)
    columns_free_space //= 3

    # generate template
    printing_template = '{:<' + str(title_width + columns_free_space) + '}'
    for hdr in header_names[1:]:
        printing_template += '{:<' + str(len(hdr) + columns_free_space) + '}'

    # print header
    print('\n\n\n')
    print('фіскальний чек'.capitalize().center(width, '~'))
    print('магазин "все для дому"'.upper().center(width))
    print(printing_template.format(*header_names))

    # print items and compute aggregated values
    total_quantity = 0
    total_cost = Decimal()

    for title, quantity, price in items:
        title_shortened = textwrap.shorten(
            title,
            width=title_width,
            placeholder='...').ljust(title_width, '.')

        quantity = int(quantity)
        price = quantized(price)

        item_total_cost = quantized(price * quantity)

        total_quantity += quantity
        total_cost += item_total_cost

        print(printing_template.format(
            title_shortened, quantity,
            price, item_total_cost))

    # print total
    print('~' * width)
    print(printing_template.format(
        'ВСЬОГО',
        total_quantity,
        'x',
        total_cost
        )
    )

    # print footer
    print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(width))
    print('\n\n')


# print_receipt([
#     ('some long item omiiit', '3', '6.66666'),
#     ('short name', '7', '5.45555')])
print_receipt(get_items())

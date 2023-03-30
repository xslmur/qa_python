# Задача 2.
# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
# {"citos": 47.999, "BB_studio" 42.999, "mo-no": 49.999, "my-main-service": 37.245, "buy-now": 38.324, "x-store": 37.166, "the-partner": 38.988, "store-123": 37.720, "roze-tka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких потрапляють в діапазон між мінімальною і максимальною ціною.
# Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service".

prices = {'citos': 47.999, 'BB_studio': 42.999, 'mo-no': 49.999, 'my-main-service': 37.245, 'buy-now': 38.324, 'x-store': 37.166, 'the-partner': 38.988, 'store-123': 37.720, 'roze-tka': 38.003}

lower_limit = 35.9
upper_limit = 40.0

matches = []
for store, price in prices.items():
    # if price >= lower_limit and  price <= upper_limit:
    if lower_limit <= price <= upper_limit:
        matches.append(store)

if matches:
    print('match:', ', '.join(matches))
else:
    print('no matches found.')

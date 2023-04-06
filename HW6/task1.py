# QA Automation Python 14.03.2023
# Karpynska Karolina
#  ДЗ 5. Робота зі словниками, отриманими з інтернету
# є url https://dummyjson.com/users  (100 сторінок)
# вивести в консоль середній вік чоловіків з Brown волоссям,
# а також сформувати список людей, що проживають в місті Louisville

import requests

def get_users():
    BASE_URL = 'https://dummyjson.com/users'
    SKIP_URL = BASE_URL + '?skip={}'

    data = requests.get(BASE_URL).json()

    total = data['total']
    users = data['users']
    while len(users) < total:
        data = requests.get(SKIP_URL.format(len(users))).json()
        users += data['users']

    return users

users = get_users()

brown_males_age = 0
brown_males_count = 0
users_from_louisville = []

for user in users:
    if user.get('gender') == 'male' and user.get('hair', {}).get('color') == 'Brown':
        brown_males_count += 1
        brown_males_age += user.get('age', 0)
    if user.get('address').get('city') == 'Louisville':
        users_from_louisville.append(user)

print('average age for males with brown hair:', brown_males_age / brown_males_count)

print('users from Louisville:')
for user in users_from_louisville:
    print(user['id'], user['firstName'], user['lastName'])

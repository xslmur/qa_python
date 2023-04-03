# Візьміть код з заняття і доопрацюйте натупним чином:
# користувач має вгадати чизло за певну кількість спроб. користувач на початку програми визначає кількість спроб
# додайте підказки. якщо рвзнися між числами більше 10 - "холодно", від 10 до 5 - "тепло", 1-4 - "гаряче"
from random import randint

def get_ai_number():
    number = randint(1, 10)
    print(f'AI: {number}')
    return number


def get_attempts_count():

    while True:
        try:
            attempts =  int(input('Enter attempts count(int): '))
            if attempts <= 0:
                print('Must be positive!')
                continue
            return attempts
        except ValueError:
            print('Number please!')


def get_user_number():

    while True:
        try:
            return int(input('Enter the number (int): '))
        except ValueError:
            print('Number please!')


def check_numbers(ai_number, user_number):
    result = ai_number == user_number
    print(f'Result is: {result}')
    return result


def get_proximity_str(ai_number, user_number):
    diff = abs(ai_number - user_number)
    if diff > 10:
        return 'Cold'
    elif diff >= 5: #5-10
        return 'Warm'
    else: #1-4
        return 'Hot'


def show_hint(ai_number, user_number, attempts_count):
    proximity_str = get_proximity_str(ai_number, user_number)
    print(f'{proximity_str}, try again! (attempt left: {attempts_count})')


def game_guess_number():
    print('Game begins!')

    attempts_count =  get_attempts_count()
    ai_number = get_ai_number()

    while attempts_count > 0:
        user_number = get_user_number()
        is_game_end = check_numbers(ai_number, user_number)
        if is_game_end:
            break

        attempts_count -= 1

        if attempts_count:
            show_hint(ai_number, user_number, attempts_count)

    if attempts_count > 0:
        print('User win')
    else:
        print('AI win ')

game_guess_number()

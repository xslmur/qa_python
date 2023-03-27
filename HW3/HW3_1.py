# QA Automation Python 14.03.2023
# Karpynska Karolina
# task3

# Задача 1. Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є буква "о" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "о".

symbols_to_match = ('O', 'o', 'О', 'о')  # latin and cyrillic o. both cases
while True:
    word = input("Enter a word that contains the letter 'o': ")
    #print('word: ', word)
    found = False
    for symbol in word:
        #print('symbol: ', symbol)
        if symbol in symbols_to_match:
            #print('matched')
            found = True
            break
    #print('found:  ', found)
    if found:
        print("Thank you! You typed a word with the letter 'o'")
        break

    print("You have entered a word without the letter 'o'. Try again.")
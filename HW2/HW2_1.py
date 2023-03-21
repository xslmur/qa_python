# QA Automation Python 14.03.2023
# Karpynska Karolina
# task2.1

# Задача 1. Сформуйте стрінг, в якому міститься інформація про певне слово.
# "Word [тут слово] has [тут довжина слова, отримайте з самого слова] letters", наприклад "Word 'Python' has 6 letters".
# # Для отримання слова для аналізу скористайтеся константою або функцією input().

# варінт написання коду через константу
word = 'Python'
length = len(word)
string = f"word '{word}' has {length} letters"
print(string)

#  варіант написання коду через функцію input()
word = input('введіть слово: ')
length = len(word)
string = f"word '{word}' has {length} letters."
print(string)
# Задача 2. Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2),
# який містить лише змінні типу стрінг, які присутні в lst1.
# Зауважте, що lst1 не є статичним і може формуватися динамічно від запуску до запуску.

# а)
list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = [elem for elem in list1 if isinstance(elem, str)]
print(list2)

# b)
# list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# list2 = []
# for item in list1:
#     #if isinstance(item,str):
#     if type(item) == str:
#         list2.append(item)
# print(list2)
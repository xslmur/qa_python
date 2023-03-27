# Задача 3. Є стрінг з певним текстом (можна скористатися input або константою).
# Напишіть код, який визначить кількість слів в цьому тексті, які закінчуються на "о" (враховуються як великі так і маленькі).

text = input('Enter text:')
#text = "zero небо zerO небО"
symbols_to_match = ('O', 'o', 'О', 'о')  # latin and cyrillic o. both cases
count = 0
for word in text.split():
    if word.endswith(symbols_to_match):
        count += 1
print("Number of words ending with 'o':", count)

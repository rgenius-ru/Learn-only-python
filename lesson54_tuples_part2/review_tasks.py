# Урок 54 - Кортежи. Часть 2. Обзор задач.
# Lesson 54 - Tuples. Part 2. Review tasks.


# Задание6 - вывести из кортежа цифры которые повторяются чаще 2-х
# раз
print('Задание6')
numbers = (32, 32, 33, 31, 32, 34, 34, 55, 55, 55)

for element in numbers:
    if numbers.count(element) > 2:
        print(element)

print()

# Задание10 - создать кортеж с определенным набором чисел и вывести
# рандомное
import random

print('Задание10')
numbers = (132, 32, 33, 31, 232, 34, 134, 155, 255, 55)
i = random.randint(0, 9)

print(i, numbers[i])
print()

# Задание11 - создать произвольный кортеж и посчитать сколько в нём
# слов и сколько чисел
print('Задание11')
heap = (13.2, 32, 33, 31, 232, 'чт', "пт")

count_numbers = 0
count_words = 0

for element in heap:
    if type(element) == type(0.0) or type(element) == type(0):
        count_numbers = count_numbers + 1  # count_number += 1

    if type(element) == type(''):
        count_words = count_words + 1  # count_words += 1

print('Чисел:', count_numbers, 'Слов:', count_words)

# Урок 54 - Кортежи. Часть 2. Обзор задач.
# Lesson 54 - Tuples. Part 2. Review tasks.

# Задание6 - вывести из кортежа цифры которые повторяются чаще 2-х
# раз

numbers = (32, 32, 33, 31, 32, 34, 34, 55, 55, 55)

for element in numbers:
    if numbers.count(element) > 2:
        print(element)


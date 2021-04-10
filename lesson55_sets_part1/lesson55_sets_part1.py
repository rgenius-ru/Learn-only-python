# Урок 55 - Наборы (Множества). Часть 1
# Lesson 55 - Sets. Part 1
# Таблица: "Типы данных" - https://vk.cc/aBWHhi
import random


print('Обзор темы наборы (множества) - set')

numbers1 = 1, 2, 2, 3
numbers2 = 2, 3, 5

unique_numbers = []

for element in numbers1 + numbers2:  # 1, 2, 2, 3, 2, 3, 5
    if element not in unique_numbers:
        unique_numbers.append(element)  # [1, 2, 3, 5]

print(unique_numbers)

unique_numbers_set = set(numbers1 + numbers2)
print(unique_numbers_set)

names = 'Максим', 'Виктор', 'Александр', 'Максим', 'Виктор', 'Павел'
unique_names_set = set(names)
print(unique_names_set)

random_numbers = random.sample(random.randint(1, 4), 4, )

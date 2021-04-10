# Урок 55 - Наборы (Множества). Часть 1
# Lesson 55 - Sets. Part 1
# Таблица: "Типы данных" - https://vk.cc/aBWHhi

print('Обзор темы наборы (множества) - set')

numbers1 = 1, 2, 2, 3
numbers2 = 2, 3, 4

unique_numbers = []

for element in numbers1 + numbers2:
    if element not in unique_numbers:
        unique_numbers.append(element)

unique_numbers_set = set((numbers1 + numbers2))
print(unique_numbers_set)

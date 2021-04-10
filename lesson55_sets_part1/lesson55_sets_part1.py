# Урок 55 - Наборы (Множества). Часть 1
# Lesson 55 - Sets. Part 1
# Таблица: "Типы данных" - https://vk.cc/aBWHhi


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

random_numbers = [2, 1, 1, 3, 3, 4, 1, 2, 2, 2]
random_numbers_set = set(random_numbers)
print(random_numbers_set)

class_substances = 'тетрагидропиранилциклопентилтетрагидропиридопиридиновые'
class_substances_set = set(class_substances)
print(class_substances_set)
print(len(class_substances_set))


list_groups = ['ЁП', 'Чёткие приколы', 'Четкие Приколы', 'Корпорация зла',
               'Палата №6', 'Лайфхак', 'Психология отношений', '5 лучших фильмов']

group_lisa = ['ЁП', 'Чёткие приколы', 'Четкие Приколы', 'Корпорация зла']
group_kira = ['Чёткие приколы', 'Четкие Приколы', 'Корпорация зла']
group_masha = ['Корпорация зла', 'Палата №6', 'Лайфхак', 'Психология отношений']

common_groups = ['Корпорация зла']  # пересечение

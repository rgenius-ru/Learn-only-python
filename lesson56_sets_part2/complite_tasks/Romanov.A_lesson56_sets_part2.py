# Урок 56 - Наборы (Множества). Часть 2
# Lesson 56 - Sets. Part 2
# Основные операции над множествами (наборами)


#1 A | В
#  A.union(В)
#  Объединение. Возвращает множество, являющееся объединением множеств A и B

#2 A = A | B  # или A |= B (x = x + 1 -> x += 1)
#  A.update(В)
#  Объединение. Добавляет все элементы массива B в множество A

#3 A & B
#  A.intersection(В)
#  Пересечение. Возвращает набор, являющийся пересечением множеств A и B

#4 A &= B
#  A.intersection_update(В)
#  Пересечение. Оставить в множестве A только элементы, принадлежащие множеству B

# 5A - B
#  A.difference(В)
#  Вычитание. Возвращает результат вычитания B из А (элементы, включенные в A , но не включены в B ).

# 6A -= B
#  A.difference_update(В)
#  Вычитание. Удаляет все элементы множества B из множества A

#7 A ^ B
#  A.symmetric_difference(В)
#  Симметричное вычитание. Возвращает симметричную разность множеств A и B (все элементы
#  Не принадлежащие A и B одновременно).

#8 A ^= B
#  A.symmetric_difference_update(В)
#  Симметричное вычитание. Сохранит в A симметричную разность множеств A и B

#9 A <= B
#  A.issubset(В)
#  Сравнение. Возвращает True если A является подмножеством B

# 10 A >= B
#  A.issuperset(В)
#  Сравнение. Возвращает True если B является подмножеством A

#11 A < B
#  Сравнение. Эквивалентно A <= B and A != B

#12 A > B
#  Сравнение. Эквивалентно A >= B and A != B


# Задание. Написать к каждой операции над множествами по одному примеру.
A = {'красный', 'грузовик', 'двухместный', 'новый'}
B = {'красный', 'минивэн', 'трёхместный'}

# result_set = set()

# Пример 1.
# A | В
result_set = A | B
print('A | B', result_set)

# Пример 2.
#  A.update(В)
result_set1 = A.update(B)
print("A.update(B)", result_set1)

# Пример 3.
# A & B
result_set2 =  A & B
print("# A & B", result_set2)

# Пример 4.
# A &= B
#result_set3 = A &= B
#print("A &= B", result_set3)

# Пример 5.
# A - B
result_set4 = A - B
print("A - B", result_set4)

# Пример 6.
# A -= B
#result_set5 = A -= B
#print("A -= B", result_set5)

# Пример 7.
# A ^ B
result_set7 = A ^ B
print("A ^ B", result_set7)

# Пример 8.
# A ^= B
#result_set8 = A ^= B
#print("A ^= B", result_set8)

# Пример 9.
# A <= B
result_set9 = A <= B
print("A <= B", result_set9)

# Пример 10.
# A >= B
result_set10 = A >= B
print("A >= B", result_set10)

# Пример 11.
# A < B
result_set11 = A < B
print("A < B", result_set11)

# Пример 12.
# A > B
result_set12 = A > B
print("A > B", result_set12)


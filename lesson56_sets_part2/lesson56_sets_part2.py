# Урок 56 - Наборы (Множества). Часть 2
# Lesson 56 - Sets. Part 2
# Основные операции над множествами (наборами)


# A | В
#  A.union(В)
#  Объединение. Возвращает множество, являющееся объединением множеств A и B

# A = A | B  # или A |= B (x = x + 1 -> x += 1)
#  A.update(В)
#  Объединение. Добавляет все элементы массива B в множество A

# A & B
#  A.intersection(В)
#  Пересечение. Возвращает набор, являющийся пересечением множеств A и B

# A &= B
#  A.intersection_update(В)
#  Пересечение. Оставить в множестве A только элементы, принадлежащие множеству B

# A - B
#  A.difference(В)
#  Вычитание. Возвращает результат вычитания B из А (элементы, включенные в A , но не включены в B ).

# A -= B
#  A.difference_update(В)
#  Вычитание. Удаляет все элементы множества B из множества A

# A ^ B
#  A.symmetric_difference(В)
#  Симметричное вычитание. Возвращает симметричную разность множеств A и B (все элементы
#  Не принадлежащие A и B одновременно).

# A ^= B
#  A.symmetric_difference_update(В)
#  Симметричное вычитание. Сохранит в A симметричную разность множеств A и B

# A <= B
#  A.issubset(В)
#  Сравнение. Возвращает True если A является подмножеством B

# A >= B
#  A.issuperset(В)
#  Сравнение. Возвращает True если B является подмножеством A

# A < B
#  Сравнение. Эквивалентно A <= B and A != B

# A > B
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

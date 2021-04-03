# Урок 53 - Кортежи. Часть 1
# Lesson 53 - Tuples. Part 1

# создание кортежей
tuple1 = ()
tuple2 = (1, 2, 'hello')
tuple3 = 3, 4, 'John'
tuple4 = tuple('hello there')

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4))

print(1, 4, "Hello", 3.14)  # в функции параметры передаются в виде кортежа

print(tuple3.index('John'))

names = 'john', 'helen', 'john'
print(names.count('john'))


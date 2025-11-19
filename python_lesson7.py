# Задача 1: Создание и вывод множества
# Создайте множество с числами: {5, 2, 8, 2, 5, 1, 9, 2}
# 1. Выведите множество (дубликаты должны исчезнуть)
# 2. Выведите количество элементов в множестве
# 3. Проверьте, есть ли число 5 в множестве (используйте in)
# 4. Проверьте, есть ли число 100 в множестве

# num = {5, 2, 8, 2, 5, 1, 9, 2}
# print(set(num))
# print(len(num))
# print(5 in num)
# print(100 in num)


# Задача 2: Операции со множествами
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# a = set1.intersection(set2)
# print(a)

# d = set1.union(set2)
# print(d)

# f = set1.difference(set2)
# print(f)



# Задача 3: Удаление дубликатов из списка
# s = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple', 'date']
# print(set(s))
# print(len(set(s)))
# print(list(set(s)))


# Задача 4: Создание и вывод словаря
# name = {
#     'name': 'Александр',
#     'age': 20,
#     'city': 'Алматы',
#     'grade': 95
#  }
# print(name)
# print(name['age'])

# name ['email'] = 'alex@gmail.com'
# print(name)



# Задача 5: Изменение и удаление в словаре
# name = {'name': 'Мария', 'age': 25, 'city': 'Астана', 'job': 'Teacher'}
# print(name)

# name ['age'] = 26
# print(name)

# name ['city'] = 'Кокшетау'
# print(name)

# name.pop('job')
# print(name)



# Задача 6: Добавление методов к словарю (с циклом)
# program = {'Python': 8, 'Java': 7, 'C++': 6, 'JavaScript': 9}
# for key in program:
#     print(key)
# for n, a in program.items():
#     print(f'{n}: {a}')
# for n, a in program.items():
#     print(f'{n}-популярность {a}')
# for n, a in program.items():
#     if a >= 8:
#         print(f"Самая высокая популярность у {n} - {a}")




# Задача 7: Добавление элементов в множество (с циклом)
# Попросите пользователя ввести 5 чисел
# Используя цикл while, добавьте все числа в множество
# Выведите множество (без дубликатов)
# Выведите количество уникальных чисел
num = input('Введите число: ')
b = num
while b in range(5):
    print()
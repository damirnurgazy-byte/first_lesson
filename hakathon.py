# Задача 11: Подсчет длин слов
# 1. Напишите функцию word_lengths(text)
# 2. Подсчитывает длину каждого слова
# 3. Возвращает словарь {'слово': длина}
#
# Примеры:
# word_lengths("hello world") → {'hello': 5, 'world': 5}
# word_lengths("Python programming") → {'Python': 6, 'programming': 11}
# word_lengths("a") → {'a': 1}

# def word_lengths(text):
#     word = text.split()
#     word_lengths = {}
#     for i in word:
#         word_lengths[i] = len(i)
#     return word_lengths

# print(word_lengths("hello world"))
# print(word_lengths("Python programming"))
# print(word_lengths("a"))


# Задача 12: Декоратор для добавления времени выполнения
# 1. Создайте декоратор measure_time(func)
# 2. Выводит сколько времени выполнялась функция
# 3. Используйте time.time()
#
# Пример:
# @measure_time
# def slow_function():
#     time.sleep(2)
#     return "Done"
#
# slow_function()
# Вывод: Время выполнения: 2.00 секунд
#        Done

# import time

# def measure_time(func):
#     def wappers(*args, **kwarges):
#         start_time = time.time()
#         result = func(*args, **kwarges)
#         end_time = time.time()
#         lead_time = end_time - start_time
#         print(f'Время выполнения: {lead_time:.2f} секунд')
#         return result
#     return wappers

# @measure_time
# def slow_function():
#     time.sleep(2)
#     return "Done"
# slow_function()



# Задача 13: Декоратор для преобразования в верхний регистр
# 1. Создайте декоратор uppercase_result(func)
# 2. Преобразует результат функции в верхний регистр
# 3. Примените к функции message(text)
#
# Пример:
# @uppercase_result
# def message(text):
#     return text
#
# message('hello world') → "HELLO WORLD"
# message('test') → "TEST"

# def uppercase_result(func):
#     def wappers(*args, **kwarges):
#         result = func(*args, **kwarges)
#         return result.upper()
#     return wappers

# @uppercase_result
# def message(text):
#     return text

# print(message('hello world'))
# print(message('test'))



# Задача 14: Функция с *args для произведения
# 1. Напишите функцию multiply_all(*args)
# 2. Перемножает все переданные числа
# 3. Используйте цикл или функцию reduce()
#
# Примеры:
# multiply_all(2, 3, 4) → 24
# multiply_all(5, 10) → 50
# multiply_all(1, 1, 1) → 1
# multiply_all(2, 3, 4, 5) → 120

# from functools import reduce

# def multiply_all_reduce(*args):
#     if not args:
#         return 1
#     return reduce(lambda x, y: x * y, args)

# print(multiply_all_reduce(2, 3, 4))
# print(multiply_all_reduce(5, 10))
# print(multiply_all_reduce(1, 1, 1))
# print(multiply_all_reduce(2, 3, 4, 5))


# Задача 15: Функция с *args для конкатенации строк
# 1. Напишите функцию concat_strings(*args)
# 2. Объединяет все строки в одну
# 3. Разделяет пробелом
#
# Примеры:
# concat_strings('Hello', 'World') → "Hello World"
# concat_strings('Python', 'is', 'awesome') → "Python is awesome"
# concat_strings('Test') → "Test"

def concat_strings(*args):
    return ' '.join(args)
print(concat_strings('Hello', 'World'))
print(concat_strings('Python', 'is', 'awesome'))
print(concat_strings('Test'))
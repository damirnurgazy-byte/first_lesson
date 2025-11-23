# # Задача 4: Работа со срезами списка
# spec = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(f'{spec[0:3]} \n{spec[-3:]} \n{spec[1:7]} \n{spec[::2]} \n{spec[::-1]} \n{spec[2:5]}')



# Задача 5: Фильтрация списка слов
# program = ['python', 'java', 'c++', 'javascript', 'go', 'rust']
# for i in range(len(program)):
#     if program[i].startswith('j'):
#         print(f'Индекс: {i}, слово: {program[i]}')

# for w in program:
#     if len(w) > 4:
#         print('Слова больше 4 символов:',w)

# for o in program:
#     print('Первый символ: ', o[0])

# for u in program:
#     print('Верхнем регистре:', u.upper())

# print('Объедененный:', ','.join(program))

# give = program[:3]
# gu = '|'.join(give)
# print("Объядинение через '|':", gu)


# Задача 6: Проверка и модификация текста
# words = input('Введите текст: ')
# if words and words[0].isupper():
#     print('Певрвая буква за гланвая:', words)
# else:
#     print('Первая буква не за главная!!!')
# print('Пробел на подчеркивание:', words.replace(' ', '-'))
# print('Все буквы за главные:', words.upper())

# print(f'Первая слово:"{words.split()[0]}"')
# print(f'Последнее слово:"{words.split()[-1]}"')
# print(f'Количество слов:"{len(words.split())}"')
# print(f'Первая слово:"{words.split()[0]}-{words.split()[-1]}"')


# Задача 7: Работа с товарами и ценами
# prices = [150, 200, 175, 300, 250, 180, 220]

# expensive_items = []
# for pri in prices:
#     if pri > 200:
#         expensive_items.append(pri)
# print("Товары дороже 200:", expensive_items)

# quantity = []
# for pp in prices:
#     if pp >= 180 and pp <= 250:
#         quantity.append(pp)
# print('Цены от 180 до 250:', len(quantity))

# max_prices = max(prices)
# max_index = prices.index(max_prices)
# print(f'Самый дорогой товар: {max_prices}, позиция: {max_index}')

# prices.sort()
# print('Сортировка цен:', prices)

# print('Первые 3 самые дешевые:', prices[0:3])
# print('Последние 2 самые дорогие:', prices[-2:])

# soom = sum(prices)
# print('Общая сумма: ',soom)

# average_cost = soom / len(prices)
# print('Вычсесление средней стомости: ', average_cost)



# Задача 8: Анализ списка логинов
# loggin = ['admin123', 'user_2024', 'test@mail', 'john_doe', 'alex.smith']
# how_many = 0
# for how in loggin:
#     if how.count('_'):
#         how_many += 1
# print('Сколько логинов содержат нижние подчеркивание:', how_many)

# how =0
# for h in loggin:
#     if h.count('.'):
#         how += 1
# print('Сколько логинов содержить точку:', how)


# max_loggin= max(loggin, key=len)
# print('Максимально длинный логин:', max_loggin)

# for log in loggin:
#     print('Первый символ каждого логина: ',log[0])

# for r in loggin:
#     print(f'Замена "@" на "#" в каждом логине: {r.replace('@', '#')}')


# a_u_startswith = []
# for s in loggin:
#     if s.startswith('a') or s.startswith('u'):
#         a_u_startswith.append(s)
# print('Логины начинающие на a и u: ',a_u_startswith)

# up = []
# for u in loggin:
#     up.append(u.upper())
# print('Вывод всех логгинов в верхнем регистре: ', up)

# jj = '|'.join(loggin)
# print('Все логины объеденны через "|": ',jj)



# Задача 9: Проверка данных студента
# data = [18, 'Александр', 92, True, 'ACTIVE']

# age = data[0]
# name = data[1]
# score = data[2]
# status = data[4]

# if age >= 18 and status == 'ACTIVE':
#     print("Студент принят")
# else:
#     print("Студент не принят")

# first_letter = name[0]
# rest_len = len(name) - 1
# print(f"{first_letter}.{('*' * rest_len)}")

# if score >= 90:
#     print("Отличник")
# elif score >= 75:
#     print("Хорошист")
# else:
#     print("Нужна помощь")

# if status.lower() == 'active':
#     print("Статус активен")
# else:
#     print("Статус не активен")




# Задача 10: Комплексная работа со строками и списками
user_input = input("Введите список товаров через запятую: ")
items = user_input.split(', ')

for i in range(len(items)):
    items[i] = items[i].capitalize()

print(len(items))
items.sort()
print(items[0:2])
print(items[-1])
longest_item = max(items, key=len)
print(longest_item)
joined_items = " | ".join(items)
joined_items = joined_items.replace(' ', '_')
print(joined_items.upper())

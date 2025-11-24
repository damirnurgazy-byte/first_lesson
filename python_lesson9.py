# Задача 1: Лотерея
# import random

# loto = []
# while len(loto) < 5:
#     num = random.randint(1, 50)
#     if num not in loto:
#         loto.append(num)


# user_number = []
# while len(user_number) < 5:
#     num = int(input('Введите число 1 до 50:'))
#     if num not in user_number:
#         user_number.append(num)
# print('Числа которые вы ввели:',user_number)
# print('Выйграшное число в лотереи:',loto)

# set_u = set(user_number)
# set_l = set(loto)
# set1 = set_u.intersection(set_l)
# print('Вы угадали число: 'set1)
# print(f"Вы угадали {len(set1)} из 5 чисел")


# Задача 2: Случайное расписание класса
# import random

# shool_tem = ['Математика', 'Физика', 'История', 'Английский', 'Биология']

# while True:
#     random.shuffle(shool_tem)
#     print(shool_tem)

#     print('Расписание на день: ')
#     ind = 1
#     for i in shool_tem:
#         print(f"{ind} {i}")
#         ind += 1
    
#     zap = input("Хотете ещё расписание? д/н:").strip().lower()
#     if zap != "да":
#         print('Вывход из программы')
#         break


# Задача 3: Розыгрыш призов с логированием
# import random
# import datetime
# import time

# name = ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
# print(name)
# priz = ['Ноутбук', 'Смартфон', 'Наушники', 'Монитор', 'Клавиатура']
# while name:
#     n = random.choice(name)
#     p = random.choice(priz)
#     print(f"Имя победителя: {n} \nПриз: {p}")

#     name.remove(input('Введите имя: '))
#     print('Имя удалено', name)

#     now = datetime.datetime.now()
#     print(f'Сегодня: [{now}] "{n}" выйграл(a) "{p}"')

#     time.sleep(2)


# Задача 4: Тестирование скорости ввода
# 1. Используя string.ascii_letters и string.digits, создайте случайный текст из 20 символов
# 2. Выведите этот текст на экран
# 3. Попросите пользователя перепечатать текст
# 4. Измерьте время используя time.time()
# 5. Проверьте совпадает ли введенный текст с оригиналом
# 6. Выведите результаты:
#    "Время: X.XX секунд"
#    "Правильность: Y%"
#    "Скорость: Z символов в секунду"

import string
import random

words = string.ascii_letters + string.digits

pp = ''
for _ in range(20):
    text = random.choice(words)
    pp += text
print(pp)

now_txt = input('Перепеайте текст: ')

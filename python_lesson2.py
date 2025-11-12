# Задача-1.
# Просите балл из 100

# score = int(input('Введите балл из 100: '))
# if 90 <= score <= 100:
#     great = 'A'
# elif 80 <= score < 89:
#     great = 'B'
# elif 70 <= score < 79:
#     great = 'C'
# elif 60 <= score < 69:
#     great = 'D'
# elif 0 <= score < 60:
#     great = 'F'
# print(f' Ваша оценка: {great }')




# Задача-2
# Просите возраст и проверяете:

# age = int(input('Введите ваш возраст: '))
# if age <= 13:
#     status = 'Ребенок'
# elif 13 > age <= 17:
#     status = 'Подросток'
# elif 18 <= age <= 64:
#     status = 'Взрослый'
# elif age >= 65:
#     status = 'Пенсионер, деда, отдыхай :3'
# print(f'Вы уже: {status}')


# Задача-3
# Просит число

# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print('Число четное: ')
# else:
#     print('Число не четное: ')




# Задача-4
# Просите логин и пароль

# log = (input('Введите логин: '))
# password = input('Введите пароль: ')

# if log == 'admin' and password == '1234':
#     print('Вход выполнен успешно')
# else:
#     print('Неверный логин или пароль')




# Задача-5
# Просите час (от 0 до 23)

# hour = int(input('Введите время 0 до 23: '))
# if hour >= 0 and hour <= 11:
#     print('Утро')
# elif hour >= 12 and hour <= 17:
#     print('День')
# else:
#     print('Ночь')



# Задача-6
# Просите температуру

# temp = int(input('Введите температуру: '))
# if temp < 0:
#     print('Холодно')
# elif temp >=0 and temp <= 15:
#     print('Прохладно')
# elif temp >= 16 and temp <= 25:
#     print('Комфортно')
# else:
#     print('Жарко')



# Задача-7
# Просите скорость автомобиля

# speed = int(input('Введите скорость: '))
# if speed <= 60:
#     print('Скорость в норме')
# elif speed > 60 and speed <= 80:
#     print('Предупреждение')
# else:
#     print('Штраф 500 тенге')



# Задача-8
# Просите возраст и доход (зарплату)

# age = int(input('Введите ваш возрасть: '))
# money = int(input('Введите ваш доход: '))
# if age >= 21 and money >= 50000:
#     print('Кредит одобрен')
# else:
#     print('В кредите отказано')




# Задача-9
# Просите сумму покупки

# sum = int(input('Введите сумму покупки: '))
# if sum < 1000:
#     skid = 0
# elif sum > 1000 and sum <= 5000:
#     skid = 0.05
# elif sum > 5000 and sum <= 10000:
#     skid = 0.10
# elif sum > 10000:
#     skid = 0.15
# itog = sum * (1 - skid)
# print(f"К оплате: {itog:.1f} тинге (скидка {skid:.0%})")



# Задача-10
# Просите возраст и стаж работы (в годах)

# age = int(input('Введите ваш возраст: '))
# work_exp = int(input('Введите ваш стаж работы: '))
# if age >= 25 and work_exp >= 3:
#     print("Вы можете работать менеджером!")
# elif age < 25 and work_exp >= 3:
#      print("Вам нужно быть старше 25 лет")
# elif age >= 25 and work_exp < 3:
#      print("Вам нужен стаж минимум 3 года")
# else:
#      print("К сожалению, вы не подходите")

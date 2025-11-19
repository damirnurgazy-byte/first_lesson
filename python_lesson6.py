#Задача 1: Простой счетчик
# N = int(input('Введите число: '))
# while N < 1:
#     print(N)


#Задача 2: Обратный отсчет
# N = int(input('Введите число: '))
# i = N
# while i >1:
#     i-=1
#     print(f'{i}')



# Задача 3: Сумма чисел
# N = int(input('Введите число: '))
# summa = 0
# i = 1
# while i < 1:
#     summa = summa + i
#     i+=1
#     print(f'Сумма= {summa}')



# Задача 4: Перебор списка с индексом
# l = [10, 20, 30, 40, 50]
# i = 0
# while i < len(l):
#     print(f"Индекс {i}: {l[i]}")
#     i +=1


# Пример 5: Перебор списка

# # Печатаем элементы списка
# fruits = ['яблоко', 'банан', 'апельсин']
# index = 0

# while index < len(fruits):
#     print(fruits[index])
#     index = index + 1

# Задача 5: Поиск элемента в списке
# Создайте список: ['Python', 'Java', 'C++', 'JavaScript', 'Go']
# Попросите пользователя ввести язык программирования
# Используя while, найдите этот язык в списке
# Если найден - выведите его индекс
# Если не найден - выведите "Язык не найден"

program = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
name_program = input('Введите язык програвмирование: ')
i = 0
while i < len(program):
    if [i] == program:
        print(i)
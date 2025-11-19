# Задача 1: Сортировка и разворот списка
# list = ['banana', 'apple', 'cherry', 'date', 'elderberry']
# list.sort()
# list.reverse()
# print(list)
# for fruct in list:
#     if fruct.upper:
#         print(fruct.upper())
# vowel_count = 0
# for word in list:
#     if word[0] in 'a, e, o':
#         print(word)
#         vowel_count += 1
# print(vowel_count)



# Задача 2: Обработка и очистка данных
# work = [' hello ', '  world  ', ' python ']
#
# for dell in work:
#     print(dell.replace(' ', '')) #insert()
#
# for rep in work:
#     print(rep.replace(' ', '-'))
#
# for low in work:
#     print(low.upper())
#
# work.clear()
# print(list)



#Задача 3: Поиск и подсчет элементов
# num = [1, 5, 2, 8, 5, 3, 5, 9, 5, 2]
# pozishn = num.index(5)
# print('Индекс сыфры пять это:', pozishn)
# five = num.count(5)
# print('Цыфра пять встречается:', five)
# for i in range(len(num)):
#     if num[i] == 5:
#         print('Число пять находиться в этих интекцах:',i)
# num.remove(5)
# print('Удалите первое вхождение 5:', num)



# Задача 4: Работа с индексами и таблицей
# students = ['Алиса', 'Боб', 'Виктор', 'Галина', 'Дмитрий']
# for i in range(len(students)):
#     print(f'{i+1}.{students[i]}')
# for i in range(len(students)):
#     if students[i] == 'Виктор':
#         print(f"Номер студента 'Виктор':{i+1}")
# students.insert(2, 'Евгени')
# print(students)
# for i in range(len(students)):
#     print(f'{i+1}.{students[i]}')


# # Задача 5: Преобразование списка чисел   
# number = [2, 4, 6, 8, 10, 12, 15, 18, 20]
# num = [x*5 for x in number]
# print(f'Исходный список:{number} \nУмноженный на 5:{num}')

# n = [x ** 2 for x in number]
# print(f'Числа в квадрате:{n}')

# na_tri = [x for x in number if x % 3 ==0]
# print(f'Числа, деляшая на 3:{na_tri}')

# soom = num+n
# print('Объедененый первые два списка:', soom)

# Задача 6: Анализ длины слов и манипуляция строками
# Создайте список слов: ['python', 'javascript', 'go', 'rust', 'java', 'cpp']
# 1. Найдите самое длинное слово
# 2. Найдите самое короткое слово
# 3. Используя цикл, выведите каждое слово с его:
#    - Первой буквой
#    - Последней буквой
#    - Длиной
# 4. Создайте новый список слов в верхнем регистре
# 5. Подсчитайте количество слов, которые содержат букву 'p'

name_program = ['python', 'javascript', 'go', 'rust', 'java', 'cpp']
name = ''
maximum_word = 0

for i in name_program:
    if len(i) > maximum_word:
        maximum_word = len(i)
        name = i
print("Самое длинное слово:", name)

short_word = name_program[0]
shortest_length = len(name_program[0])
for n in range(1, len(name_program)):
    if len(name_program[n]) < shortest_length:
        shortest_length = len(name_program[n])
        short_word = name_program[n]
print('Самое короткое слово:', short_word)

for word in name_program:
    print(f"{word}: первая= {word[0]}, последняя= {word[-1]}, длина= {len(word)}")

upper_words = []
for word in name_program:
    upper_words.append(word.upper())

print(upper_words)
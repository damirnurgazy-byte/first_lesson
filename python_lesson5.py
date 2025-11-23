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
# name_program = ['python', 'javascript', 'go', 'rust', 'java', 'cpp']
# name = ''
# maximum_word = 0

# for i in name_program:
#     if len(i) > maximum_word:
#         maximum_word = len(i)
#         name = i
# print("Самое длинное слово:", name)

# short_word = name_program[0]
# shortest_length = len(name_program[0])
# for n in range(1, len(name_program)):
#     if len(name_program[n]) < shortest_length:
#         shortest_length = len(name_program[n])
#         short_word = name_program[n]
# print('Самое короткое слово:', short_word)

# for word in name_program:
#     print(f"{word}: первая= {word[0]}, последняя= {word[-1]}, длина= {len(word)}")

# upper_words = []
# for word in name_program:
#     upper_words.append(word.upper())

# print(upper_words)


# count = []
# for c in name_program:
#     count.append(c.count('p'))
# print('Буква "p" встречается: ', count)



# Задача 7: Таблица умножения с вложенными циклами
# print("Таблица умножения 2: ")
# for i in range(1, 11):
#     print(f"{i} * 2 = {i * 2}")

# print('Таблица умножение 5: ')
# for i in range(1,11):
#    print(f'{i} * 5 = {i*5}')

# print("Таблица 2: ", end="")
# for i in range(1, 11):
#     print(f"{i} * 2 = {i * 2}", end="")
#     if i !=10:
#         print(", ", end="")
# print()

# print('Таблица 5: ', end="")
# for i in range(1, 11):
#     print(f"{i} * 5 = {i*5}", end="")
#     if i !=10:
#         print(", ", end="")
# print()


# all__products = []
# for num in [2, 5]:
#     print(f"Таблица умножение {num}: ", end="")
#     for i in range(1, 11):
#         product = num * i
#         all__products.append(product)
#         print(f"{num} * {i} = {product}", end="")
#         if i !=10:
#             print(", ", end="")
#     print()


# count = 0
# for cc in all__products:
#     if 20 < cc < 30:
#         count += 1
#         print(f"Количество произведений больше 20 и меньше 30: {count}")

# max_products = max(all__products)
# print(f"Максимальная прозйведение: {max_products}")




# Задача 8: Комплексная работа с методами
# num_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# num_list.sort()
# print(f"Отсортированный список: {num_list}")

# num_list.reverse()
# print(f"Перевернутый список: {num_list}")

# print(f"Подчет: {len(num_list)}")

# num_count = num_list.count(5)
# print(f"Число пять встречается: {num_count}")

# num_index = num_list.index(1)
# print(f"Индекс числа 1: {num_index}")

# num_list.remove(1)
# print(f"Удаление первого числа: {num_list}")




# Задача 9: Поиск и фильтрация текста
# phrase_list = ['Привет мир', 'Python очень крутой', 'Я люблю программирование', 'Это отлично', 'JavaScript сложный']

# phrase_o = []
# for ph in phrase_list:
#     if 'o' and 'о' in ph: #Англиская "o" и русская "о"
#         phrase_o.append(ph)
# print(f'Фразы содержащие букву "o": {phrase_o}')


# now_phrase = []
# for now in phrase_list:
#     if len(now) > 20:
#         now_phrase.append(now)
# print(f"Новая список с длиной 20 символов: {now_phrase}")


# phrase_replase = []
# for rp in phrase_list:
#     phrase_replase.append(rp.replace(' ', '-'))
# print(f'Заменил все проблы на подчеркивание: {phrase_replase}')


# phrase_first = []
# for first in phrase_list:
#     words = first.split()
#     phrase_first.append(words[0])
# print("Первые слова фраз:", phrase_first)


# len_phrase = 0
# for ph in phrase_list:
#     words = ph.split()
#     len_phrase += len(words)
# print("Общее количество слов во всех фразах:", len_phrase)



# Задача 10: Вложенные циклы и комбинирование данных
# Создайте списки:
# numbers = [1, 2, 3, 4]
# letters = ['a', 'b', 'c']
#
# 1. Создайте новый список, где каждое число соединено с каждой буквой
#    Результат: ['1a', '1b', '1c', '2a', '2b', '2c', ...]
#
# 2. Создайте новый список со строками "число-буква" для пар:
#    ['1-a', '2-b', '3-c', '4-?']
#    (если букв меньше, пропустите оставшиеся числа)
#
# 3. Для каждой пары выведите информацию
#
# 4. Используйте extend() для объединения списков


numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c']

combined = []
for num in numbers:
    for letter in letters:
        combined.append(str(num) + letter)
print("Все комбинации число-буква:", combined)

paired = []
for i in range(min(len(numbers), len(letters))):
    paired.append(f"{numbers[i]}-{letters[i]}")
print("Пары число-буква:", paired)

for pair in paired:
    print("Пара:", pair)

extra_numbers = [5, 6]
numbers.extend(extra_numbers)
print("Объединённый список чисел:", numbers)

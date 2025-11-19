# #Задача 1: Преобразование текста
# name = input('Введите текст: ')
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())



# Задача 2: Проверка содержимого строки
# t = input('Введите текст: ')
# print(t.isalpha())

# s = input('Введите сыфры: ')
# print(s.isdigit())

# l = ['кошка', 'матрешка', 'каша', 'моенез']
# print(f"длина списка: {len(l)}")




# Задача 3: Замена текста
# text = input('Введите предложение: ')
# word_for_replace = input('Введите слова для замены: ')
# new_word = input('Введите новое слово: ')

# print(text.replace(word_for_replace, new_word))


# Задача 4: Разделение и объединение строк
# text = input('Введите слова: ')
# j = text.split()
# print(f"Количсева слов: {len(j)}")
# print("-".join(j))



# Задача 5: Проверка начала и конца строки
# fail = input('Введите имя файла на букву а: ')
# if fail.lower().startswith('a') and fail.endswith('.txt'):
#     print('Имя файла свотвесвует')
# elif not fail.lower().startswith('a'):
#     print('Имя должно начинаться на букву а!')
# elif not fail.endswith('.txt'):
#     print('Вы забыли указать, что это файл (.txt)')




#Задача 6: Работа со списком студентов
# student_name = ['Костя', 'Леша', 'Аяжан', 'Бекарыс', 'Байжан']
# print('Список студентов:')
# print(student_name[0])
# print(student_name[1])
# print(student_name[2])
# print(student_name[3])
# print(student_name[4])
# print(f'Всего студентов в списке: {len(student_name)}')
# student_name.append(input('Введите имя нового студента: '))
# student_name.append(input('Введите имя ещё одного: '))
# student_name.append(input('Введите имя последнего: '))
# print('\nОбновлённый список студентов:')
# print(student_name[0])
# print(student_name[1])
# print(student_name[2])
# print(student_name[3])
# print(student_name[4])
# print(student_name[5])
# print(student_name[6])
# print(student_name[7])
# print(f'Всего студентов в списке: {len(student_name)}')




# Задача 7: Удаление и поиск в списке
# fruts = ['яблоко', 'банан', 'апельсин', 'груша', 'банан']
# print('Список фруктов: ', fruts)
# fr = input('Введите название фрукта: ')
# if fr in fruts:
#     index = fruts.index(fr)
#     print(f'Индекс фрукта "{fr}": {index}')
# else:
#     print(f'Фрукт "{fr}" не найден в списке')

# hoy_fruts = input('Введи название фрукта которое повторяется: ' )
# if hoy_fruts in fruts:
#     count = fruts.count(hoy_fruts)
#     print(f'Этот фрукт "{hoy_fruts}" встречается: {count} раз')
# else:
#     print(f'Фрукт "{hoy_fruts}" не найден в списке!')

# dell = input('Введи название фрукта которое хотите убрать: ' )
# if dell in fruts:
#     rem = fruts.remove(dell)
#     print(f'Этот фрукт "{dell}" убран! \nВот обнавленный список {fruts}')
# else:
#     dell != fruts
#     print(f'Такгого "{dell}" фрукта нету в списке!')



# Задача 8: Сортировка и разворот списка
# num = [5, 2, 9, 1, 7, 3]
# print(num)
# num.sort()
# print(num)
# num.reverse()
# print(num)




# Задача 9: Вставка и удаление элементов
# absd = ['А', 'Б', 'Г', 'Д']
# print(absd)
# absd.insert(2,'B')
# print(absd)
# absd.pop(1)
# print(absd)




# Задача 10: Объединение методов строк и списков
# Попросите пользователя ввести предложение со словами через пробел
# 1. Переведите в нижний регистр (lower)
# 2. Разделите на слова (split)
# 3. Отсортируйте слова по алфавиту (sort)
# 4. Выведите отсортированные слова
# 5. Объедините обратно через запятую (join)
# 6. Выведите финальный результат

words = input('Введите слова: ')
print(words)
print(words.lower())

v = words.split()
print(v)

v.sort()
print('Сортировка по алфовиту:',v)

go = ', '.join(v)
print(go)
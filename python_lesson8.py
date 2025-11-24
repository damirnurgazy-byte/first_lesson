# students_dict = {
#     'Алиса': 85,
#     'Боб': 92,
#     'Витор': 78,
 
# }
# with open('users.txt', 'w') as file:  #исправить код
#     for i in students_dict.items:

#         file.write(f'{i} {a}')   



# Задача 1: Преобразование содержимого файла
# with open('text.txt', 'r') as file:
#     text = file.read()
#     upp = text.upper()
#     print(f'{text}\n{upp}')
# with open('text_upper.txt', 'w') as now_file:
#     now_file.write('Первое сообщение')
# with open('text_upper.txt', 'r') as file:
#     now_text = file.read()    
# print(f"Оба файла:{text}, {now_text}")



# Задача 2: Слияние двух файлов
# 1. Создайте два файла:
#    - 'file1.txt' с текстом: "Первый файл"
#    - 'file2.txt' с текстом: "Второй файл"
# 2. Прочитайте содержимое обоих файлов
# 3. Объедините содержимое в одну переменную (с разделением)
# 4. Запишите объединенный текст в новый файл 'merged.txt'
# 5. Выведите содержимое объединенного файла
# Формат: "Первый файл\n---\nВторой файл"

with open('file1.txt', 'w') as f1:
    f1.write('Первый файл')
with open('file2.txt', 'w') as f2:
    f2.write('Втарой файл')
with open('file1.txt', 'r') as f1:
    text = f1.read()
    print(text)
with open('file2.txt', 'r') as f2:
    text = f2.read()
    print(text)
with open('file1.txt' + '\n++\n'+'file2.txt') as f1,f2:
    text = f1
    print(text)



#   1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые
#   пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

file = open('doc_5_1.txt', 'w')
line = input('Введите данные \n')
while line:
    file.writelines(line)
    line = input('Введите данные \n')
    if not line:
        break

file.close()
file = open('doc_5_1.txt', 'r')
content = file.readlines()
print(content)
file.close()
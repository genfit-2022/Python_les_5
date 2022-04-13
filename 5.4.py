#   4. Создать (не программно) текстовый файл со следующим содержимым:
#       One — 1
#       Two — 2
#       Three — 3
#       Four — 4
#   Напишите программу, открывающую файл на чтение и считывающую построчно данные.
#   При этом английские числительные должны заменяться на русские. Новый блок строк должен
#   записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('doc_5_4.txt', 'w', encoding='utf-8') as file_obj:
    with open('doc_5_4_1.txt', encoding='utf-8') as m_file:
        file_obj.writelines([line.replace(line.split()[0], rus.get(line.split()[0])) for line in m_file])

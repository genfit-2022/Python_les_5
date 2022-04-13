#   5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
#   Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
def summary():
    try:
        with open('doc_5_5.txt', 'w+') as file_obj:
            line = input('Введите числа, разделённые пробелом: \n')
            file_obj.writelines(line)
            my_numb = line.split()
            print('Сумма чисел: ', sum(map(int, my_numb)))
    except ValueError:
        print('Ошибка ввода!')
summary()

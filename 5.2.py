#   2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт
#   строк и слов в каждой строке.

with open('doc_5_2.txt', 'r', encoding='utf-8') as obg:
    res = [f'{line}-я строка -// {count.strip()} //- количество слов - {len(count.split())}.'
              for line, count in enumerate(obg, 1)]
    print(*res, f'Всего строк - {len(res)}.', sep='\n')
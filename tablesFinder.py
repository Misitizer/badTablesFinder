import pandas as pd
import os


def find_bad_tables(directory_path: str, tables_file: str) -> None:

    """
    Функция находит таблицы в скриптах и выводит в файле result.txt
    эти таблицы с номерами строк, в которых они находятся

    directory_path: str - входная директория. По ней будут искаться
    файлы типа .txt и .sql

    tables_file: str - файл в котором лежит список таблиц для поиска

    """

    os.chdir(directory_path)

    xls = pd.read_excel(tables_file, header=None)

    tables = [i[0].lower() for i in xls.values.tolist()]

    paths = []
    folder = [i for i in os.walk(os.getcwd())]

    for address, dirs, files in folder:
        paths = paths + [address + '\\' + file for file in files if file[-4:] == '.txt' or file[-4:] == '.sql']

    result = open('result.txt', 'w', encoding='UTF-8')
    for path in paths:
        with open(path, encoding='UTF-8') as file:
            lines, table = [], []

            for i, line in enumerate(file, start=1):
                if set(tables) & set(line.lower().split()):
                    lines.append(i)
                    table.append(list(set(tables) & set(line.lower().split()))[0])

            test = dict()
            for el in list(zip(table, lines)):
                if el[0] not in test:
                    test.update({el[0]: [el[1]]})
                else:
                    test[el[0]].append(el[1])

        result.write('\nФайл: ' + path)
        if not test:
            result.write('\n Таблицы не найдены\n')
        else:
            for key, val in test.items():
                result.write('\n Таблица: {}  Строки: {}'.format(key, val))
        result.write('\n')

    result.close()


if __name__ == "__main__":
    find_bad_tables(input(), input())
    print('\n\n\nDone')
    input()

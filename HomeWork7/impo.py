import csv
import view


def imp(list):
    with open('tabl.csv', 'a', encoding='utf-8') as f:
        file_writer = csv.writer(f, delimiter=".")
        file_writer.writerow(list)

def imp_txt(list_s):
    with open('text.txt', 'a', encoding='utf-8') as f:

        f.writelines('.'.join(list_s) + '\n')

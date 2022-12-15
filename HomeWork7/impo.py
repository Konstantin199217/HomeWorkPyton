import csv
import view


def imp(list):
    with open('tabl.csv', 'a', encoding='utf-8') as f:
        # names = (["Фамилия", "Имя", "Номер_Телефона", "Описание"])
        file_writer = csv.writer(f, delimiter=".")
        # file_writer.writerow(["Фамилия", "Имя", "Номер_Телефона", "Описание"])
        file_writer.writerow(list)


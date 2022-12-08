# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# my_text = 'Теперь Кекс доволен, он даже замурчал, \n' \
#           'ведь обновлённый дизайн ему понравился. \n' \
#           'Но где хороший дизайн, там и дополнительные правки: \n' \
#           '«добавь тексты», «вставь картинку», «поиграйся со шрифтами и отступами».\n' \
#           ' У вас хорошо получилось починить сайт. Поможете дошлифовать его?\n'
#
# print(my_text)
# new_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, my_text.split(' ')))
#
# print(" ".join(new_list))
#


# ________________________________________________________________________________
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


# with open('File.txt', 'r', encoding='utf-8') as file:
#      text = file.read()
#
# def com(text): # Зашифровали
#     str_list = []
#     count = 1
#     for i in range(len(text) - 1):
#         if text[i] == text[i + 1]:
#             count += 1
#         else:
#             str_list.append(str(count) + text[i])
#             count = 1
#     if count > 1 or (text[len(text) - 2] != text[-1]):
#         str_list.append(str(count) + text[i])
#     return str_list
# print(text)
# print(com(text))
#
# new_text = ''.join(com(text))
# # Записали
# with open('File1.txt', 'w', encoding='utf-8') as file:
#     file.write(new_text)
#
#
# with open('File1.txt', 'r', encoding='utf-8') as file:
#           text2 = file.read()
#
# print(text2)
# def decom(text):
#     new_txt = ''
#     num = 0
#     for i in range(len(text)):
#         if text[i].isnumeric():
#             num = text[i]
#         else:
#             new_txt =new_txt + text[i] * int(num)
#     return new_txt
# # a = [0 for i in range(5)]
# print(decom(text2))
# decod = decom(text2)
# with open('File2.txt', 'w', encoding='utf-8') as file:
#      file.write(decod)
# ____________________________________________________________________
# Создайте программу для игры в ""Крестики-нолики"".

b_list = list(range(1, 10))


def board():
    print('__________')
    for i in range(3):
        print('|', b_list[0 + i * 3], '|', b_list[1 + i * 3], '|', b_list[2 + i * 3], )
    print('__________')

board()
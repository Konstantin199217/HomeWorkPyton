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


# def press(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             inp_str = text.readline()
#             ind = 0
#             out_str = ''
#             count = 1
#             while ind < len(inp_str) - 1:
#                 if inp_str[ind] == inp_str[ind + 1]:
#                     count += 1
#                 else:
#                     if count == 1:
#                         res.write(inp_str[ind])
#                     else:
#                         res.write(str(count) + inp_str[ind])
#                     count = 1
#                 ind += 1
#             print(out_str)
#
# press('File.txt', 'result.txt')
# def depress(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             inp_str = text.readline()
#             count = ''
#             for letter in inp_str:
#                 if letter.isdigit():
#                     count += letter
#                 else:
#                     if not count:
#                         res.write(int(count) * letter)
#                     else:
#                         res.write(letter)
#                     count = ''
def depress(file, result):
    with open(file, 'r', encoding='utf-8') as text:
        with open(result, 'w', encoding='utf-8') as res:
            inp_str = text.readline()
            count = ''
            for letter in inp_str:
                if letter.isdigit():
                    count += letter
                else:
                    if not count:
                        res.write(int(count) * letter)
                    else:
                        res.write(letter)
                    count = ''

depress('result.txt', 'result2.txt')

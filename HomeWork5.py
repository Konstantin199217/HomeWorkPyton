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
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('File.txt', 'r', encoding='utf-8') as file:
     text = file.read()

def com(text):
    str_list = []
    count = 1
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            str_list.append(str(count) + text[i])
            count = 1
    if count > 1 or (text[len(text) - 2] != text[-1]):
        str_list.append(str(count) + text[i])
    return str_list
print(text)
print(com(text))
new_text =
with open('File1.txt', 'w', encoding='utf-8') as file:
    file.write(new_text)

# def decom(t)

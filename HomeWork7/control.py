import  view
import impo
import export

def button():
    num = view.inp()

    if num == 1:
        nam = list(input('Введите данные через точку Фамилия.Имя.Номер_телефона.Описание: ').split('.'))
        impo.imp_txt(nam)
        # impo.imp(nam)
    if num == 2:
        nam2 = input('Введите Фамилию Имя или Телефон: ')
        export.exp_txt(nam2)
        # export.exp(nam2)

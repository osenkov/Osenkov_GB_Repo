earn = input('Введите значение выручки предприятия, тыс. руб.: ')
out = input('Введите значение затрат предприятия, тыс. руб.: ')
staff = input('Введите численность персонала, чел.: ')
try:
    earn = float(earn)
    out = float(out)
    staff = int(staff)
    if earn < 0 or out < 0:
        print('Отрицательные значения данных недопустимы')
    elif staff <= 0:
        print('Введены некорректные данные численности персонала')
    elif earn < out:
        print('Предприятие отработало с убытком в размере', out - earn, 'тыс. руб.')
    elif earn == out:
        print('Предприятие не извлекло прибыль, финансовый результат', out - earn, 'тыс. руб.')
    elif earn > out:
        print()
        print('Предприятие отработало с прибылью в размере', round(earn - out, 2), 'тыс. руб.')
        print('Рентабельность выручки:', round((earn - out) / earn * 100, 2), '%')
        print('Прибыль предприятия на одного сотрудника составила', round((earn - out) / staff, 2), 'тыс. руб.')

except ValueError:
    print('Ошибка ввода')

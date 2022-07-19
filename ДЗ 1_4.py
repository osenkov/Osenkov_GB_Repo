x = input('введите целое положительное число: ')
try:
    x = int(x)
    if x < 0:
        print ("Вы ввели отрицательное число")
    else:
        tail = x % 10
        while x > 0:
            x = x // 10
            y = x % 10
            if tail >= y:
                continue
            else: tail = y
        print(f'самое большое число ={tail}')
except ValueError:
    print('Ошибка ввода')
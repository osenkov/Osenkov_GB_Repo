sec = int(input('введите время в секундах: '))
h = sec // 3600
m = (sec % 3600) // 60
s = sec % 3600 % 60
print(f"время {h}:{m}:{s}")

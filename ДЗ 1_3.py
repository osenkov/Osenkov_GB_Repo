a = int(input('введите цифру от 1 до 9: '))
b = int(f"{a}{a}")
c = int(f"{a}{a}{a}")
S = a + b + c
print(f"сумма чисел {a}+{b}+{c} = {S}")
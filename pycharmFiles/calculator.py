a = int(input()) # вводим число и сохраняем его в переменной a
b = int(input()) # вводим число и сохраняем его в переменной b
c = input() # вводим одну из 4-х операций и сохраняем её в переменной c
if c == '+': # если операция - это сложение
    print(a + b)
elif c == '-': # если операция - это вычитание
    print(a - b)
elif c == '*': # если операция - это умножение
    print(a * b)
elif c == '/': # если операция - это деление
    if b == 0: # если число b равняется 0, то
        print('На ноль делить нельзя.')
    else: # если число b не является 0, то деление успешно выполняется
        print(a / b)
else: # если операция введена неверно
    print('Неверная операция.')
age = int(input()) # вводим число полных лет
if age <= 2: # если введённый возраст меньше или равно 2, то вычисляется и выводится возраст в человеческих годах
    print(age * 10.5)
else: # если введённый возраст больше 2, то каждый год собаки равен 4
    print(2 * 10.5 + (age - 2) * 4)
num = int(input()) # вводим трёхзначное положительное число
digit1 = num % 10 # получаем последнюю цифру числа
digit2 = (num % 100) // 10 # получаем вторую цифру числа
digit3 = num // 100 # получаем первую цифру числа
print("Сумма цифр =", digit3 + digit2 + digit1) # выводится сумма цифр
print("Произведение цифр =", digit3 * digit2 * digit1) # выводится произведение цифр
a = int(input()) # вводим длины сторон треугольника и сохраняем их в переменных a, b, c
b = int(input())
c = int(input())
if a == b == c: # если все стороны равны, то треугольник равносторонний
    print('Равносторонний')
if (a == b or a == c or b == c) and (a != c or a != b or b != c): # если две стороны равны, а одна нет, то треугольник равнобедренный
    print('Равнобедренный')
if a != b and a != c and c != b: # если все стороны разные, то треугольник разносторонний
    print('Разносторонний')
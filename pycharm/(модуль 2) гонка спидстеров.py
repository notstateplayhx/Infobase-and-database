flash_speed = int(input()) # задаём скорость Флэша и сохраняем в переменной flash_speed
zoom_speed = int(input()) # задаём скорость Зума и сохраняем в переменной zoom_speed

if flash_speed < zoom_speed: # если Флэш медленнее Зума, то будет выведено NO
    print('NO')

elif zoom_speed < flash_speed: # если Зум медленнее Флэша, то будет выведено YES
    print('YES')

else: # если Флэш и Зум с одинаковой скоростью, то будет выведено Don't know
    print('Don`t know')
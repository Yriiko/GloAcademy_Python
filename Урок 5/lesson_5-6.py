# Задание 6
print('Введите номер кармана')
n = int(input())


if (n >= 1 and n <= 10 and n >= 19 and n <= 28 and n % 2 == 0) or (n >= 11 and n <= 18 and n >= 29 and n <= 36 and n % 2 != 0):
    print('черный')
else:
    print('красный')

if n == 0:
    print('зеленый')

if n > 36:
    print('ошибка ввода')

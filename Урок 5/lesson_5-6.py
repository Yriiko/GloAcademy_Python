# Задание 6
print('Введите номер кармана')
n = int(input())

if n == 0:
    print('зеленый')

elif n % 2 == 0 and 1 <= n <= 10:
    print('черный')

elif n % 2 == 0 and 19 <= n <= 28:
    print('черный')

elif n % 2 != 0 and 11 <= n <= 18:
    print('черный')

elif n % 2 != 0 and 29 <= n <= 36:
    print('черный')

elif n > 36:
    print('ошибка ввода')

else:
    print('красный')

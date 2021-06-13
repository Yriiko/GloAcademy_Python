# Задание 4
r = int(input())
k = int(input())
n = int(input())
print('За', n, 'мяча нужно заплатить', r * n +
      k * n // 100, 'рублей и', k * n % 100, 'копеек')

# Задание 3
from math import *
article_1 = input()
article_2 = input()
article_3 = input()

len_1 = len(article_1)
len_2 = len(article_2)
len_3 = len(article_3)

max_len = max(len_1, len_2, len_3)

if max_len == len_1:
    print(article_1)
elif max_len == len_2:
    print(article_2)
else:
    print(article_3)

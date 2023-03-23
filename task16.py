# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random 
# from random import randint
N = int(input('Введите N '))
my_list = []
for i in range (N):
    my_list.append(random.randint(0, N))
x = int(input('Введите число x '))
print(my_list) # массив выводится
print(my_list.count(x)) # считает кол-во числа x

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random 
N = int(input('Введите N '))
A = []
for i in range (N):
    A.append(random.randint(0, N))
x=int(input('введите заданное число x '))
number=0
for i in range(len(A)):
       if abs(x-A[i])<x-number and abs(x-A[i])>0:
        number=i
print(A) # массив выводится
print(A[number])
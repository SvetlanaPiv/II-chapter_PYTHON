# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из 
# всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input("Введите неотрицательное число - а: "))
b = int(input("Введите неотрицательное число - b: "))
def summa(a, b):
    a += 1
    b -= 1
    if b > 0:
        return summa(a, b)
    else:
        return a
print("Сумма: ", summa(a, b))

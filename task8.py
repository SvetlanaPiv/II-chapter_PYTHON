# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между 
# дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('сторона шоколадки '))
m = int(input('сторона шоколадки другая '))
k = int(input('отлом от шоколадки '))

if n * m > k and k%m ==0 or k%n==0: # делим без остатка
    print ('делится')
else:  print (' не делится')

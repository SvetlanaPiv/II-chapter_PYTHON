# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

S = int(input('Введите сумму чисел: '))
P = int(input('Введите произведение чисел: '))

X = (S-int((S**2-4*P)**0.5))//2
Y = S - X
if X>=1000 and Y>=1000:
    print('Петя обманул')
else:
    print(f'Петя загадал числа {X, Y}')

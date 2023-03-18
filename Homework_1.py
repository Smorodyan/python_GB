# Homework_1

# Задача 2: Найдите сумму цифр трехзначного числа
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

'''
num = int(input('Input a three-digit number: '))
sum = 0

print('The Sum of', num, 'is', end=' ')
if num < 100 or num > 999:
    print('This is not a three-digit number, try again!')
else:
    while num > 0:
        sum = sum + num % 10
        num = num // 10
    print(sum)
'''


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4

'''
amount = int(input('Input amount of products: '))
b = int(amount/ 3 * 2)
a = int(b/4)
print(a, b, a)
'''

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

'''
ticket = int(input('Input ticket number ' ))
count = 0
n = ticket

while n > 0:
    count +=1
    n = n // 10

if count % 2 != 0:
    print('Input another ticket number')

else:
    k = ticket
    count2 = count // 2
    sum1 = 0
    
    while count2 > 0:
        sum1 = sum1 + k % 10
        k = k // 10
        count2 = count2 - 1
    print('1-st number is', sum1)

    sum2 = 0
    while k > 0:
        sum2 = sum2 + k % 10
        k = k // 10
    print('2-nd number is', sum2)

    if sum1 == sum2:
        print('This is a lucky ticket!')
    else:
        print('This is not a lucky ticket, buy another one...')
'''
    


# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

import sys
n = int(input('n:'))
m = int(input('m:'))
k = int(input('k:'))

n1 = n
while n1 < (n * m):
    if n1 == k:
        print('yes')
        sys.exit()
    n1 = n1 + n
m1 = m
while m1 < (n * m):
    if m1 == k:
        print('yes')
        sys.exit()
    m1 = m1 + m
print('no')



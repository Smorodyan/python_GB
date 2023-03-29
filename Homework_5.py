# Homework_5


# Задача 26: 
# Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

'''
def funct(a, b, degree=1):
    degree *= a 
    if b == 1:
        return degree
    return funct(a, b - 1, degree)

a = int(input('Input a: '))
b = int(input('Input b: '))
print(funct(a, b))
'''


# Задача 28: 
# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def funct_sum(a, b, sum = 1):
    sum += 1
    if b == 1:
        return sum
    elif a == 1:
        return funct_sum(a, b - 1, sum)
    return funct_sum(a - 1, b, sum)


a = int(input('Input a: '))
b = int(input('Input b: '))
print(funct_sum(a, b))


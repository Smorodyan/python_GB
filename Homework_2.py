# #Homework_2

# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть
# Input: 5 -> 1 0 1 1 0
# Output: 2


coins = int(input('Input number of coins: '))
count_1 = 0
count_2 = 0
for i in range(coins):
    coin_side = int(input())
    if coin_side == 1:
        count_1 += 1
    else:
        count_2 += 1
if count_1 > count_2:
    print(count_2)
elif count_1 == count_2:
    print('equal')
else:
    print(count_1)

print(min(count_1,count_2))

#Добавить проверку на ввод только 1 и 0. Добавить ввод в одну строку




# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа
# 4 4 -> 2 2
# 5 6 -> 2 3

'''
import math
sum = int(input('a: '))
mult = int(input('b: '))

d = sum * sum - 4 * mult
if d < 0:
    print('The numbers are not integer')
elif d == 0:
    x = y = int(sum / 2)
    print(x, y)
else:
    x = int((sum + math.sqrt(d)) / 2)
    y = int((sum - math.sqrt(d)) / 2)
    print(x, y) 
'''


# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N
# 10 -> 1 2 4 8

'''
num = int(input('Input a number: '))
result = 1

while result < num:
    print(result, end=' ')
    result *= 2
''' 



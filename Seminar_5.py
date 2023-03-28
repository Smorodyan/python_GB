# Seminar_5

# Задача №31.
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

'''
def fib(n, a1 = 0, sum = 0, a2 = 1):
   sum = 0
   while n > 0:
   
    for i in range(2, n+2):
        sum = (a1 + a2)
        a1 = a2
        a2 = sum
        print(sum)
    # return sum

n = int(input('Input a number: '))
fib(n)
'''


# Задача №33. 
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

'''
def bad_marks(array):
    min_mark = array[0]
    max_mark = array[0]
    for i in range(len(array)):
        if array[i] < min_mark:
            min_mark = array[i]
        else:
            max_mark = array[i]
    for i in range(len(array)):
        if array[i] == max_mark:
            array[i] = min_mark
    return array

marks = '1 3 3 3 4'
array = [i for i in marks.split()]
print(bad_marks(array))
'''


# Задача №35.
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

'''
def ordinary_number(num):
    if num == 2:
        return True
    elif num % 2 != 0:
        return True

num = int(input('Input a number: '))
print(ordinary_number(num))
'''



# Задача №37. 
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


def funct(n, num=''):
   num =num + input()
   if n == 1:
      return num
   return funct(n - 1, num)
    

n = int(input('Input a number: '))
print(funct(n)[::-1])


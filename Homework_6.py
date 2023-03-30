# Homework_6

# Задача 30: 
# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

'''
def arithmetic_funct(a,b,c):
    array = []
    k = a
    for i in range(a, a+c):
        array.append(k)
        k+=b
    return array

first_element = int(input('Input a first number: '))
diffrence = int(input('Input a number for the difference: '))
quantity = int(input('Input a number of elements: '))
print(*arithmetic_funct(first_element, diffrence, quantity))
'''


# Задача 32: 
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума) min: n  max: m
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def index_range(array, min, max):
    indexes = [i for i in range(len(array)) if min <= array[i] <= max]
    return indexes   


array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = int(input('min: '))
max = int(input('max: '))
print(index_range(array, min, max))





# Seminar_6

# Задача №39. 
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит 
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# Вывод: 3 3 2 12

'''
def diff(array_1, array_2, output=[]):
    for i in array_1:
        if i not in array_2:
            output.append(i)
    return output

# array_1 = [int(input()) for i in range(int(input('Input a number of elements: ')))]
# array_2 = [int(input()) for i in range(int(input('Input a numbre of elements: ')))]
array_1 = [3, 1, 3, 4, 2, 4, 12]
array_2 = [4, 15, 43, 1, 15, 1]
   
print(diff(array_1, array_2))

# array_1 = set(array_1)
# array_2 = set(array_2)
# array_1 = array_1.difference(array_2)
# print(array_1)
# array_2 = array_2.difference(array_1)
# print(array_2)
# array_1 = array_1.union(array_2)
# print(array_1)
# print(array_1.union(array_2).difference(array_1.difference(array_2)))
'''




# Pадача №41. 
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 5
# 1 2 3 4 5 
# Вывод: 0

# Ввод: 5
# 1 5 1 5 1
# Вывод: 2

'''
def number_of_min(array):
    count = 0
    for i in range(1, len(array) - 1):
        if array[i + 1] < array[i] and array[i] > array[i + 1]:
            count += 1
    return count

array = [int(input()) for i in range(int(input('Input a number of elements: ')))]
new_array = len([array[i] for i in range(len(array)) if array[i + 1] < array[i] > array[i + 1]])
print('Output:',number_of_min(array))
'''


# Задача №43. 
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 1 2 3 2 3 
# Вывод: 2

'''
def num_of_elements(array):
    sum = 0
    count = 0
    for i in range(len(array) - 1):
        count = 0
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                count += 1
                sum += 1
                                                   
    return sum

# array = [int(input()) for i in range(int(input('Input a number of elements: ')))]
array = [1, 2, 3, 2, 1, 3, 1, 2]
print(array)
print('Output', num_of_elements(array))
'''


# Задача №45. 
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10(5). Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 300
# Вывод: 220 284


def divider(num):
    array = []
    for i in range(num):
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum += j
                array.append([i, sum])
    # print(array)

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i][0] == array[j][1] and array[i][1] == array[j][0]:
                print(array[i], array[j])


num = int(input('Input a number: '))
divider(num)




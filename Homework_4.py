# Homework_4

# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Input: 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# -> 6 12


# num_1 = int(input('Input number of elements for the first array: '))
# print('Input 1-st array: ')
# list_1 = [int(input()) for i in range(num_1)]
# num_2 = int(input('Input number of elements for the second array: '))
# print('Input 2-nd array: ')
# List_2 = [int(input()) for i in range(num_2)]
list_1 = [2, 4, 12, 8, 10, 6, 10, 8, 6, 18, 4, 2]
list_2 = [3, 6, 9, 12, 15, 18, 4]
list_3 = []
for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_1[i] == list_2[j]:
            if list_1[i] not in list_3:
                list_3.append(list_1[i])
            
print(sorted(list_3))

# Вывод по возрастанию пузырьком:
# print(list_3)
# for i in range(len(list_3)):
#     for j in range(len(list_3) - i - 1):
#         if list_3[j] > list_3[j+1]:
#             temp = list_3[j]
#             list_3[j] = list_3[j+1]
#             list_3[j+1] = temp
# print(list_3)





# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# Input: 5 -> 3 5 1 4 7
# Otput: 15

'''
num = int(input('Input nuumber of bushes:'))
berries = [int(input()) for i in range(num)]
sum = 0
volume = []

for i in range(num):
    if i == 0:
        sum = berries[i] + berries[num-1] + berries [i + 1]
    elif i == num-1:
        sum = berries[i] + berries[i - 1] + berries [0]
    else:
        sum = berries[i] + berries[i - 1] + berries [i + 1]
    volume.append(sum)
print(volume)

max = volume[0]
for i in volume:
    if i > max:
        max = i
print(max)
'''
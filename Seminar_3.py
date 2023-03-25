
# Задача №17.
# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

'''
list = [1, 1, 2, 0, -1, 3, 4, 4]
count = 0
list_new = set()
for i in range(len(list)):
    list_new.add(list[i]) 
    
print(list_new)
print('Output', len(list_new))
'''

'''
n = int(input('Input a number of elements: '))
list = [int(input()) for item in range(n)]
new_list = set(list)
print(new_list)
print(len(new_list))
'''

'''
list = [1, 1, 2, 0, -1, 3, 4, 4]
new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
print(len(new_list))
'''     



# Задача №19.
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]


# n = int(input('Input a number of elements: '))
# list = [int(input()) for item in range(n)]
# k = int(input('Input K: '))
# for i in range(k+1):
#     list.append(list.pop(0))
# print(list)


# n = int(input('Input a number of elements: '))
# list = [int(input()) for item in range(n)]
# k = int(input('Input K: '))
# part_1 = list[:k+1]
# print(part_1)
# part_2 = list[k+1:]
# print(part_2)
# new_list = part_2 + part_1
# print(new_list)
# print(list)

# n = int(input('Input a number of elements: '))
# list = [int(input()) for item in range(n)]
# k = int(input('Input K: '))
# for i in range(k):
#     list.insert(0, list.pop(-1))
# print(list)


#Example with pop:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop())
# print(list_1)

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) 




# Задача №21. 
# Напишите программу для печати всех уникальных значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
# ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

'''
dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# new_list = []
# for i in range(len(dictionary)):
#     new_list += dictionary[i].values()
# print(*set(new_list))   # *звёздочка - убирает скобки при возврате 

#new_list = set([value for dict in dictionary for value in dict.values()])
# new_list = set([value.strip() for dict in dictionary for value in dict.values()]) 
# # strip() - убирает пробелы в значении
# print(*new_list)

new_list = []
for dict in dictionary:
    for value in dict.values():
        new_list.append(value.strip())
print(*set(new_list))
'''


# Задача №23. 
# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

list = [0, -1, 5, 2, 3, 6]
count = 0
for i in range(len(list) - 1):
    if list[i+1] > list[i]:
        count += 1
print(count)
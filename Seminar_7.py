# Seminar_7

# Задача 47:
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список

'''
a = [33, 2, 33, 4, 33, 6, 33, 8, 33]
b = list(map(lambda x: x, a))
print(b)
'''



# Задача №49. 
# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию 
# find_farthest_orbit(list_of_orbits), которая среди списка орбит 
# планет найдет ту, по которой вращается самая далекая планета.
# Input: orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

'''
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
find_farthest_orbit= max(orbits, key=lambda x: x[0] * x[1] if x[0] != x[1] else False)
print(find_farthest_orbit)
'''


# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 

values = [4, 2, 10, 6] 
# same_by = []
# print(same_by)
same_by = list(filter(lambda x: True if x% 2 else False, values))
if same_by == True:
    print('Same')
else:
    print('diffrent')



# Задача_3:
# Имеется упорядоченный список
# a = [[1, 2, 3], 
# 	   [4, 5, 6], 
# 	   [7, 8, 9]]
# Перебрать все элементы этого списка с помощью функции
# enumerate и элементы, стоящие на главной диагонали заменить 0

'''
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for ind,value in enumerate(a):
    value[ind] = 0
    # for i in range(len(value)):
    #     if i == ind:
    #         a[ind][i] = 0
    print(b,c)
print(a)
'''


# Задача_4:
# Имеется список id сотрудников из 10 эл-ов, 
# каждый id - случайное число от 1 до 100 (list_comprehension)
# Имеется список имен сотрудников из 10 эл-ов (вручную)
# Сопоставить каждому имени сотрудника его id по порядку и 
# вывести получившийся список кортежей
# Отсортировать список по возрастанию id
# Вывести имена сотрудников, получившие нечетное id
   
'''
from random import randint

id = [randint( 1, 1000) for i in range(1000)]
b = ['Иванов', 'Петров', 'Матвеев', 'Трифонов', 'Быстров', 
     'Рязанов','Васичкин', 'Никифоров', 'Железов', 'Костин']
lst = list(zip(sorted(id), b))
lst = list(filter(lambda x: x[0] % 2 != 0, lst))
# for i in zip(sorted(id), b):
#     list.append(i)
        # print(i)
print(lst)
'''













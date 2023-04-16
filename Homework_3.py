# Homework_3

# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1


n = int(input('Input a number of elements: '))
array = [int(input()) for item in range(n)]
print(*array)
x = int(input('Input X: '))
count = 0
for i in range(n):
    if x == array[i]:
        count += 1
print('->', count)
print(array.count(x))





# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 6
# 1 2 6 3 4 5
# 6
# -> 5

'''
import sys
n = int(input('Input a number of elemnts: '))
array = [int(input()) for i in range(n)]
print(array)
x = int(input('Input X: '))
min_element = array[0]

if array[0] > x:
    min = array[0] - x
else:
    min = x - array[0]

for i in range(n):
    if array[i] > x:
        k = array[i] - x
        if k < min:
            min = k
            min_element = array[i]
    elif array[i] < x:
        k = x - array[i]
        if k < min:
            min = k
            min_element = array[i]
    else:
        print('the nearest element is:', array[i])
        sys.exit()
print('the nearest element is:', min_element)
'''  



# Задача 20: 
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Input: ноутбук
# Output: 12

'''
dictionary = ({1 : ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
              2 : ['D', 'G'],
              3 : ['B', 'C', 'M', 'P'],
              4 : ['F', 'H', 'V', 'W', 'Y'],
              5 : ['K'],
              8 : ['J', 'X'],
              10 : ['Q', 'Z']},
             {1 : ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
              2 : ['Д', 'К', 'Л', 'М', 'П', 'У'],
              3 : ['Б', 'Г', 'Ё', 'Ь', 'Я'],
              4 : ['Й', 'Ы'],
              5 : ['Ж', 'З', 'Х', 'Ц', 'Ч'],
              8 : ['Ш', 'Э', 'Ю'],
              10 : ['Ф', 'Щ', 'Ъ']}
            )
              
word = input('Please, input a word: ')
sum = 0
for i in word.lower():
    for n in dictionary:
        for key, value in n.items():
            for k in value:
                if i == k.lower():
                    sum += key
print('The sum of characters of the word is:', sum)
'''



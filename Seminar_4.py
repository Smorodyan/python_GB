# Seminar_4

# Задача №25. 
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

'''
quote = 'a a a b c a a d c d d'     # input('Input characters: ')
quote = quote.split()
new_quote = {}
print(quote)

for i in quote:
    if i in new_quote:
        new_quote[i] += 1
        print(f'{i}_{new_quote[i]}', end = ' ')
    else:
        new_quote[i] = 0
        print(i, end =' ')
'''      



# Задача №27.
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

'''
text = 'She sells sea shells on the sea shore\
        The shells that she sells are sea shells\
        Im sure.So if she sells sea shells on the sea shore\
        Im sure that the shells are sea shore shells'
text = text.replace('.', ' ').lower().split()
# for znak in ('.', ',', '!', ':', '?'):
#     text = text.replace(znak, ' ')
print(set(text), len(set(text)))
'''


# Задача №29. 
# Ваня и Петя поспорили, кто быстрее решит 
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не 
# такими смышлеными. Никто из ребят не смог до 
# конца сделать это задание. Они решили так: у кого 
# будет меньше ошибок в коде, тот и выиграл спор. За 
# помощью товарищи обратились к Вам, студентам.

'''
nums = [4, 5, 3, 8, 4, 3, 2, 0, 5, 4, 9, 3]
max = int(nums[0])
for i in range(len(nums)):
    if int(nums[i]) == 0:
        break
    else:
        if int(nums[i]) > max:
            max = nums[i]
print(max)
'''


array = []
i = 0
num = None

while num != 0:
    num = int(input())
    if num == 0:
        break
    array.append(num)

max = int(array[0])
for i in range(len(array)):
    if int(array[i]) == 0:
        break
    else:
        if int(array[i]) > max:
            max = array[i]
    
print(array)
print('max =', max)



# print(5, 6, 8, 9.99)

# n = 78
# print(n)
# print(type(n))

# n = 'this "is" jast \'a string'
# print(n)
# print(type(n))

# # print(type(n))
# """
# print(type(n))
# print(type(n))
# print(type(n))
# """

# a = 5
# b = 'string'
# c = 8.99

# print(a, '-', b, '-', c)
# print(a, '+', c, '=', a + c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a, b, c))


# print('input smth')
# k = input()
# print(k)

# m = int(input('input smth: '))
# print(type(m))
# print('this is: ', m)

# a = 5.83
# print(a)
# a = int(a)
# print('округлили до: ', a)


# a = 5.23432
# b = 3.532432
# print(a * b)
# print(round(a * b, 3))

# a = 5
# a **= 2
# print(a)

# a = 2 < 5 and 6 > 5
# print(a)


# username = input('Input name: ')
# if username == 'Masha':
#     print('Hi Masha!')
# elif username == 'Pasha':
#     print('Hi Pasha!')
# elif username == 'Misha':
#     print('Hi Misha')
# else: print('Hi', username)


# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i +=  1
# else:
#     print('Stop')    
# print(i)


# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1



# for i in 1, -2, 3, 14, 5:
#     print(i)

# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7
# r = range(100, 0, -20) # 100 80 60 40 20

# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#     print(i)

# a = 'qwerty'
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)



text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
print(text[2:9] + text[-5] + text[:2]) # ...

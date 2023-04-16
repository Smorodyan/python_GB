# def sum_numbers(n, m):
#     print(m, end = ' ')
#     summ = 0
#     for i in range(1, n+1):
#         summ += i
#     # print(summ)
#     return summ

# # sum_numbers(5)
# n = int(input('n: '))
# m = input('m: ')
# print(sum_numbers(n, m))

# nums = [i for i in range(int(input()))]
# nums = [int(input()) for i in range(int(input()))]
# print(nums)

# # a = [i for i in range(1, 9)]
# # b = [i for i in range(6, 13)]
# a = [1, 2, 3, 4, 5, 3, 7, 1, 6, 7, 8] 
# b = [6, 7, 1, 8, 6, 8, 9, 10, 11, 12]
# a = set(a)
# b = set(b)
# b.intersection(a)
# print(b)
# b = list(b)
# print(*sorted(b))
# # print(f'{a} \n{b}')



# a = [[1, 2], [3, 4, 5], [8,[9, 0]]]
# print(a[0]) # [1, 2]
# print(a[0][1]) # 2
# print(a[1][2]) # 5
# print(a[2][1][0]) # 9


# array_1 = [int(input()) for i in range(int(input('Input a number of elements: ')))]
# array_2 = [int(input()) for i in range(int(input('Input a numbre of elements: ')))]
# array_3 = [i for i in array_1 if i not in array_2]


# a = [1, 2 ,3, 5, 8, 15, 23, 38]
# b=[]
# for i in a:
#     if i % 2 == 0:
#        b.append([i, i**2])
# print(b)


# data = '1 2 4 9 3 9 5 2 4'
# data = list(map(int, data.split()))
# print(data)

a = [i for i in range(1, 10) if i % 2 == 0]
print(a)
a = [i if i % 2 == 0 else 33 for i in range(1, 10)]
print(a)


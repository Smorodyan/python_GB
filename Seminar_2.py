
# Задача №9. 
# По данному целому неотрицательному n вычислите 
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл 
# while
# Input: 5
# Output: 120 

'''
num = int(input('Input factorial number: '))
count = 1
factorial = 1

if num == 0:
    print("1")
while count <= num:
    factorial *= count
    count += 1
print(f'Factorial of {num} = {factorial}')
'''



# Задача №11. 
# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не 
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

'''
num = int(input('Input a num for Fibonachi: '))
count = 0
a = 1
b = 2

#print(0,a,a,b, end=' ')
while b < num:
    b = b + a
    #print(b, end=' ')
    a = b - a
    count += 1
    
if b == num:
        print('fib =',count + 4)
else:
      print(-1)
'''



# Задача №13.
# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю 
# наблюдений за погодой. Они обратились к синоптикам, а те, в 
# свою очередь, занялись исследованиями статистики за 
# прошлые годы. Их интересует, сколько дней длилась самая 
# длинная оттепель. Оттепелью они называют период, в 
# который среднесуточная температура ежедневно превышала 
# 0 градусов Цельсия. Напишите программу, помогающую 
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

'''
days = int(input('Input quantity of days: '))
day_temperature = None
count = 1
hot_days = 0
num_of_hot_days = 0
output_data = 0

while count <= days:  
    day_temperature = int(input('Day: '))
    count += 1
    if day_temperature > 0:
        hot_days += 1
        if num_of_hot_days > hot_days:
            output_data = num_of_hot_days
        else:
            output_data = hot_days
        num_of_hot_days = hot_days
    elif day_temperature < 0:
        hot_days = 0
   
print('Number of hot days is:', output_data)
'''



# Задача №15. 
# 15. Иван Васильевич пришел на рынок и решил 
# купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз 
# потяжелей, а для тещи полегче. Но вот незадача: 
# арбузов слишком много и он не знает как же выбрать 
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9


# amount = int(input('Input namber of watermwlons: '))
max_weight = None
min_weight = None
# for i in range(2, amount):
for i in 5, 1, 6, 5, 9:
    print(i, end=' ')
    if max_weight == None and min_weight == None:
        max_weight = i
        min_weight = i
    if max_weight < i:
        max_weight = i
    elif min_weight > i:
        min_weight = i
print()
print(f'min waight = {min_weight} and max waight = {max_weight}')
    



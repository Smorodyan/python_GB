# Задача №1. 
# За день машина проезжает n километров. Сколько 
# дней нужно, чтобы проехать маршрут длиной m 
# километров? При решении этой задачи нельзя 
# пользоваться условной инструкцией if и циклами.

'''
#import math # Подключение мат. библиотеки
n = int(input('Input a distance km per day for the car: '))
m = int(input('Input all the distance: '))
k = int(m / n)
print(k + int(bool(m % n)))
#print(math.ceil(m/n)) # мат. функция, округляет в большую сторону
'''


# Задача №3. 
# В некоторой школе решили набрать три новых 
# математических класса и оборудовать кабинеты для 
# них новыми партами. За каждой партой может сидеть 
# два учащихся. Известно количество учащихся в 
# каждом из трех классов. Выведите наименьшее 
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

'''
firstClass = int(input('Input number of student for the 1-st class: '))
secondClass = int(input('Input number of student for the 2-nd class: '))
thirdClass = int(input('Input number of student for the 3-rd class: '))
print((firstClass // 2 + firstClass % 2) + 
      (secondClass // 2 + secondClass % 2) +
      (thirdClass // 2 + thirdClass % 2))
# print((firstClass + 1) // 2 + 
#        (secondClass + 1) // 2 + 
#        (thirdClass + 1) // 2)
'''


# Задача №5.
# Вагоны в электричке пронумерованы натуральными 
# числами, начиная с 1 (при этом иногда вагоны 
# нумеруются от «головы» поезда, а иногда – с 
# «хвоста»; это зависит от того, в какую сторону едет 
# электричка). В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, 
# что его вагон имеет номер j. Он хочет определить, 
# сколько всего вагонов в электричке. Напишите 
# программу, которая будет это делать или сообщать, 
# что без дополнительной информации это сделать 
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

'''
i = int(input('Input a first number: '))
j = int(input('Input a secound number: '))
if i == j:
    print('We need additional information')
else: print(i + j - 1)
'''


# Задача №7.
# Дано натуральное число. Требуется определить, 
# является ли год с данным номером високосным. Если 
# год является високосным, то выведите YES, иначе 
# выведите NO. Напомним, что в соответствии с 
# григорианским календарем, год является 
# високосным, если его номер кратен 4, но не кратен 
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

'''
year = int(input('Input a year: '))

if year % 100 == 0:
    if year % 400 == 0:
        print('This is a leap year')
    else:
        print('This year is not a leap year')    
elif year % 4 == 0:
    print('This is a leap year')
else:
    print('This year is not a leap year')
'''

# Задача 
# Шахматный конь ходит буквой Г. Даны две различные клетки
# шахматной доски. Определите, может ли конь попасть с 
# первой клетки на вторую одним ходом. В случае, если
# хотя бы одно из введенных чисел не лежит в диапазоне
# от 1 до 8, выведите строку "Ошибка!"


x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))

if (1 > (x1 or x2 or y1 or y2) > 9):
    print('Error!')
elif abs(x1 - x2) == 1 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1 or abs(y1 - y2) == 2:
    print('You can take this step!')
else: print("You cannot take this step")


# Задача 
# Треугольник существует только тогда, когда сумма любых
# двух его сторон больше третьей. Дано a,b,c - стороны
# треугольника. Требуется сравнить длинну каждого
# отрезка-сторонны с суммой двух других. Если хотя бы
# в одном случае отрезок окажется больше суммы двух
# других, то треугольника с такими сторонами не существует

'''
a = int(input('Input size a: '))
b = int(input('Input size b: '))
c = int(input('Input size c: '))

if ((a + b) < c) or ((a + c) < b) or ((b + c) < a):
    print('This is not a triangle')
else:
    print("This is a triangle")
'''

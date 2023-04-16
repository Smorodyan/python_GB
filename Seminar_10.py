# 1. Создать класс, описывающий человека. Должны быть поля для имени, фамилии и возраста.
# Создать экземпляр и вывести информацию о человеке.

# 2. Доработать предыдущий класс, чтобы вся информация о человеке была доступна 
# при вызове str над экземпляром

# 3. Добавить метод greet, вызов которого будет выводить в консоль информацию о человеке в формате
# "Привет! Меня зовут Петров Василий, мне 12 лету".


# 4. Добавить атрибут grades, в котором будет храниться список оценок.
# Создать список учеников, заполняя оценки случайными числами и вывести информацию о них в порядке
# убывания среднего балла.
# Заполнение оценок и подсчет среднего балла вынести в отдельные методы.



# from statistics import mean

# class Human:
#     def __init__(self, name, surname, age, grades: list):
#         self.name = name
#         self.age = age
#         self.surname = surname
#         self.grades = grades
#     def __str__(self):
#         return f'{self.name}, {self.surname}, {self.age}'
    
#     def greet(self):
#         print(f'Привет! Меня зовут {self.name} {self.surname}, мне {self.age} лет')
#     # def __eq__(self, other):
#     #     if type(other) == Human:
#     #         if self.age == other.age:
#     #             return "одногодки они"
#     #         else:
#     #             return "разного возраста они"
#     #     if type(other) == int:
#     #         return "человек не цифра"
#     # def __add__(self, other):
#     #     return other.age + self.age
#     def average(self):
#         sredn = mean(self.grades)
#         return sredn
#     def __repr__(self) -> str:
#         return f'{self.name} {self.surname}'
#     def rand_mark(self):
#         import random
#         rand_num = random.randint(1, 5)
#         self.grades.append(rand_num)
#         return 
    
# ivan = Human("Иван", "корич", 20, [4,2,5,5])
# max_ = Human("Максим", "голуб", 23, [4,2,5,2])
# andre = Human("Андрей", "зелен", 30, [4,2,5,4])

# students = [ivan, max_, andre]
# new_students = sorted(students, key=lambda x: x.average(), reverse=True)

# print(ivan)
# ivan.greet()
# print(new_students)

# for i in students:
#     i.average()



    # 5. Создайте класс прямоугольник - Rectangle.
# Метод __init___ принимает две точки - левый верхний и правый нижний угол.
# Каждая точка представлена экземпляром класса Point.
# Реализуйте методы вычисления площади и периметра прямоугольника.


# 6. Добавьте в класс Rectangle метод has_point. Метод принимает точку на плоскости и возвращает True,
# если точка находится внутри прямоугольника и False в противном случае


# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b        

# class Rectangle:
#     def __init__(self, x: Point, y: Point):
#         self.x = x
#         self.y = y
#     def get_perim(self):
#         return (abs(self.x.a - self.x.b) + abs(self.y.b - self.y.b))*2
#     def get_squre(self):
#         return abs(self.x.a - self.x.b) * abs(self.y.b - self.y.b)
#     def has_point(self):
#         point_x = int(input("X = "))
#         point_y = int(input("Y = "))
#         if self.x.a <= point_x <= self.x.b and self.y.b <= point_y <= self.y.b:
#             return True
#         else:
#             return False



# p1 = Point(1, 1)
# p2 = Point(10, 10)

# rect = Rectangle(p1, p2)
# print(rect.x.a)
# print(rect.get_perim())
# print(rect.get_squre())

# print(rect.has_point())



class Dragon:
    def __init__(self, height, flammability, color):
        self.height = height
        self.flammability = flammability
        self.color = color
    def str(self) -> str:
        return print(f'Dragon with height {self.height}, flammability {self.flammability} and {self.color} color')
    def change_color(self, new_color):
        self.color = new_color


dr = Dragon(175, 10, 'green')
dr1 = Dragon(83, 10, 'blue')

dr.str()
dr1.str()
dr.change_color('white')
dr.str()



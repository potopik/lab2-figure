import math
from abc import ABC


class Figures(ABC):
    def per(self): pass         # Периметр

    def area(self): pass        # Площадь

    def __repr__(self): pass    # Вывод


class Dot:
    def __init__(self):             # Инициализация
        self.cord = []
        if n > 1:
            for i in range(n):
                a = float(input(f'Введите координату {i + 1}: '))
                self.cord.append(a)
        else:
            ro = float(input('Введите расстояние от начала координат точки: '))
            fi = float(input('Введите угол точки: '))
            self.cord = [ro, fi]

    def dist(self, b):              # Расчет дистанции от точки до точки
        a = 0
        if n > 1:
            for i in range(len(self.cord) - 1):
                a += (self.cord[i] - b.cord[i]) ** 2
            a = math.sqrt(a)
        elif n == 1:
            r1 = self.cord[0]
            r2 = b.cord[0]
            a = math.sqrt(r1 ** 2 + r2 ** 2 - 2 * r1 * r2 * math.cos(self.cord[1] - b.cord[1]))
        else:
            x1 = self.cord[0] * math.sin(self.cord[1]) * math.cos(self.cord[2])
            x2 = b.cord[0] * math.sin(b.cord[1]) * math.cos(b.cord[2])
            y1 = self.cord[0] * math.sin(self.cord[1]) * math.sin(self.cord[2])
            y2 = b.cord[0] * math.sin(b.cord[1]) * math.sin(b.cord[2])
            z1 = self.cord[0] * math.cos(self.cord[1])
            z2 = b.cord[0] * math.cos(b.cord[1])
            a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        return a

    def __repr__(self):             # Вывод
        return f'{self.cord}'


class Tria(Figures):
    def __init__(self):                # Инициализация
        print('Координата первой точки:')
        self.d1 = Dot()
        print('Координата второй точки:')
        self.d2 = Dot()
        print('Координата третьей точки:')
        self.d3 = Dot()

    def per(self):                      # Расчет периметра
        return self.d1.dist(self.d2) + self.d2.dist(self.d3) + self.d1.dist(self.d3)

    def area(self):                     # Расчет площади
        p = (self.d1.dist(self.d2) + self.d2.dist(self.d3) + self.d1.dist(self.d3)) / 2
        a = self.d1.dist(self.d2)
        b = self.d2.dist(self.d3)
        c = self.d1.dist(self.d3)
        return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 8)

    def __repr__(self):                 # Вывод
        return f'\nТреугольник\n' \
               f'Координата первой точки: {self.d1}\nКоордината второй точки: {self.d2}\n' \
               f'Координата третьей точки: {self.d3}\nS = {self.area()}\nP = {self.per()}'


class Tetra(Figures):
    def __init__(self):         # Инициализация
        print('!Координаты должны быть введены строго в порядке обхода границ!'
              '\n!Также четырехугольник должен быть выпуклым!')
        print('Координата первой точки:')
        self.d1 = Dot()
        print('Координата второй точки:')
        self.d2 = Dot()
        print('Координата третьей точки:')
        self.d3 = Dot()
        print('Координата четвертой точки:')
        self.d4 = Dot()

    def per(self):              # Расчет периметра
        return self.d1.dist(self.d2) + self.d2.dist(self.d3) + self.d3.dist(self.d4) + self.d4.dist(self.d1)

    def area(self):             # Расчет площади
        p1 = (self.d1.dist(self.d2) + self.d2.dist(self.d3) + self.d1.dist(self.d3)) / 2
        a1 = self.d1.dist(self.d2)
        b1 = self.d2.dist(self.d3)
        c1 = self.d1.dist(self.d3)
        p2 = (self.d1.dist(self.d4) + self.d1.dist(self.d3) + self.d3.dist(self.d4)) / 2
        a2 = self.d1.dist(self.d4)
        b2 = self.d1.dist(self.d3)
        c2 = self.d3.dist(self.d4)
        s1 = math.sqrt(p1 * (p1 - a1) * (p1 - b1) * (p1 - c1))
        s2 = math.sqrt(p2 * (p2 - a2) * (p2 - b2) * (p2 - c2))
        return round(s1 + s2, 8)

    def __repr__(self):        # Вывод
        return f'\nЧетырехугольник\n' \
               f'Координата первой точки: {self.d1}\nКоордината второй точки: {self.d2}\n' \
               f'Координата третьей точки: {self.d3}\nКоордината третьей точки: {self.d4}' \
               f'\nS = {self.area()}\nP = {self.per()}'


class Circle(Figures):
    def __init__(self):     # Инициализация
        print('Координата центра окружности:')
        self.o = Dot()
        self.r = float(input('Радиус окружности: '))

    def per(self):          # Расчет периметра
        return 2 * math.pi * self.r

    def area(self):         # Расчет площади
        return math.pi * self.r ** 2

    def __repr__(self):     # Вывод
        return f'\nОкружность\n' \
               f'Координата центра: {self.o}\nR = {self.r}\nS = {self.area()}\nP = {self.per()}'


figures = list()    # Лист для фигур
while True:
    try:
        n = int(input('В каком пространстве вы хотите работать? (n - натуральное число)'
              '\nn > 1 -- n-мерное пространство'
              '\nn < 1 -- полярная система координат'
              '\nn = '))
    except ValueError:
        print('Введено некорректное значение.\nПопробуйте снова\n')
        continue
    else:
        print('Обработка запроса')
    break

while True:     # Диалог с пользователем и ввод данных
    q = input('''Что вы хотите ввести?
    Треугольник     -- 1
    Четырехугольник -- 2
    Окружность      -- 3
    Введите q для выхода
--''')

    if q == 'q':
        break
    elif q == '1':
        figures.append(Tria())
    elif q == '2':
        figures.append(Tetra())
    elif q == '3':
        figures.append(Circle())


sorted_f = list()
areas = list()
for i in figures:
    areas.append(i.area())
areas.sort()

for s in areas:
    for j in figures:
        if j.area() == s:
            sorted_f.append(j)
            figures.remove(j)
            continue
figures = sorted_f

for f in figures:  
    print(f)

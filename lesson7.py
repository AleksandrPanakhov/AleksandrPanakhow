#Урок 1
#Задание1
a = "hello"
b = "everyone"
print(f"{a}, {b}")
numb1 = int(input("Enter any number: "))
numb2 = int(input("Enter any number one more time: "))
print(f"You have chosen the numbers {numb1} and {numb2}")
word = input("Enter any word: ")
print(f"{word} - it's good choise")

#Задание2
time = int(input("Enter the time in seconds: "))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")

#Задание3
n = input("Enter an integer: ")

while n < '0':
    print("I've asked for number greater than 0! Please, try again!")
    n = input('Please enter number greater than 0: ')

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

#Задание4
def num_max(num):
    if num < 10:
        return num
    else:
        m = num_max(num // 10)
        return m if m > % 10 else  num % 10

print(f"The largest number is: {num_max(int(input('Enter the number: ')))}")

#Задание6
while True:
    days = 1
    start_km = float(input("Стартовый результат: "))
    last_km = float(input("Финальный результат: "))
    if start_km <= 0 or last_km < 0
        print("Резуьтат должен быть больше нуля. Стартовое значение != 0.")
    else:
        while start_km < last_km:
        start_km += start_km * 0.1
        days += 1
        print(f"Спортсмен добьется результата за {days} дней")
        break
#Урок 2
#Задание1
my_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4],
           (5, 6, 6.6), {7: 'seven', 8: 'eight'}, {9, 10},
frozenset(), range(11), b'twelwe', bytearray(b'thirteen'),
zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError]

for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")

#Задание2
my_list = list(input("Enter the numbers without spaces - "))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)

#Задание3

month = int(input("Введите месяц: "))
month_dict = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
month_list = ["январь", "февраль", "март", "апрель", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

if month in month_dict:
    print(f"{month})-й месяц года - это {month_dict[month]}")
    print(f"{month}-й месяц года - это {month_list[month - 1]}")
else:
    print("Error.")
#Задание4

string = input("Enter the numbers with space - ").split()

for n, i in enumerate(string, 1):
    print(n, i) if len (i) <= 10 else print(n, (i[:10]))

#Урок 3
#Задание1

def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "Division by zero forbidden!"
    return round(div_num, 4)
print(div(input("Enter first number - "), input("Enter second - ")))

#Задание2

def person_inf(name, surname, birthday, city, email, phone):
    return f"Name - {name}; Surname - {surname}; birthday - {birthday}; city - {city}; email - {email}; phone - {phone}"

print(person_inf(name="Aleksandr", surname="Panakhov", birthday="25.04.1995", city="Moscow", email="saniok178@mail.ru", phone="89296903811"))

#Задание3
def my_func(num_1, nun_2, num_3):
    my_list = [num_1, nun_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError
        return "Enter only numbers"

print(my_func(2, 11, -30))

#Задание4

def my_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Enter a float number and negative power"
    return res

print(my_pow_fun(4.5, -2))

#Задание5

def sum_num():
    s = 0
    while True:
        in_list = input("Enter a number, input 'q' to exit: ").split()
        for num in in_list:
            if num in in_list:
                if num == "q":
                    return s
                else:
                    try:
                        s += int(num)
                    except ValueError:
                        print("To exit the program, enter 'q'.")
                print(f"Sum of numbers = {s}")
    print(sum_num())

#Задание6

def int_func():
    for word in input("Enter words with a space (lower latin script):\n").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - only small Eng letters!")
    int_func()

#Урок4
#Задание1

from sys import argv

def salary()
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Salary - {time * rate + bonus}")
    except ValueError:
        print("Enter 3 numbers. Not string or empty character.")

salary()

#Задание2

my_list = [15, 16, 2, 3, 1, 7, 5,  4, 10]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)

#Задание3

uniq_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(uniq_list)

#Задание4

from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Sours list\n{my_list}\nNo repetition list\n{uniq_list}")

#Задание5
from functools import reduce

def mul_list(el_1, el_2):
    return el_1 * el_2

uniq_list = [el for el in range(100, 1001, 2)]
print(f"List\n{uniq_list}\nMultiplication of numbers\n{reduce(mul_list, uniq_list)}")

#Задание6

#Урок5
#Задание1

my_file = open("text_1.txt", 'w', encoding='utf-8')
line = " "
while line:
    line = input("Напиши или не пиши!: ")
    my_file.write(f"{line}\n") if line != '' else my_file.close()

#Задание2

with open("text_1.txt", "r", encoding='utf-8') as f_obj:
    usefulness = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов' for line, count in enumerate(f_obj ,1)]
    print(*usefulness, f"Всего строк - {len(usefulness)}.", sep="\n")

#Задание3

with open('оклад.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)} \n'
    f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')

#Задание4

rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("ex4.txt", "w", encoding='utf-8') as new_file:
    new_file.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in my_file])

#Задание5

from random import randint

with open('ex5.txt', mode='w+', encoding='utf-8') as the_file:
    the_file.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
    the_file.seek(0)
    print(sum(map(int, the_file.readline().split())))

#Задание6
subj = {}
with open('ex6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.replace('-', '0').replace(':', '').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '')
        subj[line.split()[0]]  = sum(map(int, line.split()[1:]))
    print(f'Общее количество часов по предмету: \n{subj}')

#Урок6
#Задание1

class Trafficlight
    __color = "Черный"

    def running(self):
        while True:
            print("Trafficlight is red now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)
            print("Trafficlight is green now")
            sleep(7)
            print("Trafficlight is yellow now")
            sleep(2)

trafficlight = Trafficlight()
trafficlight.running()

#Задание2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def get_full_profit(self):
        return f"{self._length} м * 25 кг * 25 см = {(self._length * self._width *25 *5) / 1000} т"

    road_1 = Road(5000, 20)
    print(road_1.gett_full_profit())

#Задание3
 class Worker:
     def __init__(self, name, surname, position, wage, bonus):
         self.name = name
         self.surname = surname
         self.position = position
         self._income = {"profit": wage, "bonus": bonus}

class Position(Worker)
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_full_profit(self):
        return f"{sum(self._income.values())}"

manager = Position("Aleksandr", "Panakhov", "CEO", 500000, 125000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())

#Задание4

class Car:
    "Автомобиль"

def __init__(self, name, color, speed, is_police=False):
    self.name = name
    self.color = color
    self.speed = speed
    self.is_police = is_police
    print(f'Новая машина: {self.name} (цвет {self.color}) машина полицейская - {self.is_police}')

def go(self):
    print(f'{self.name}: Машина поехала.')
def stop(self):
    print(f'{self.name}: Машина остановилась.')
def turn(self, direction):
    print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}.')
def show_speed(self):
    return f'{self.name}: Скорость автомобиля: {self.speed}.'

class TownCar(Car):
    "Городской автомобиль"

def show_speed(self):
    return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
        if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"

class WorkCar(Car):
    "Грузовой автомобиль"
 def show_speed(self):
     return f'{self.name}: Скорость автомобиля {self.speed}. Превышение скорости!' \
         if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"

class SportCar(Car):
    "Спортивный автомобиль"


class PoliceCar(Car)
    "Полицейский автомобиль"
def __init__(self, name, color, speed, is_police=True)
    super().__init__(name,color, speed, is_police)

police_car = PoliceCar ('"Полицай"', 'голубой', 90)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar ('"Грузовичкофф"', 'желтый', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()
print()

sport_car = SportCar ('"Молния"', 'красный', 205)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('"Джеповоз"', 'белый', 50)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()
print()

#Задание5
class Stationery:
    def __init__(self, title="Чем-то из этого можно писать"):
        self.title = title

    def draw(self):
        print(f"Начни писать {self.titile} ")

class Pen(Stationery)
    def draw(self):
        print(f"Начни с {self.title} ручки")
class Pencil(Stationery)
    def draw(self):
        print(f"Начни с {self.title} карандаша")

class Marker(Stationery)
    def draw(self):
        print(f"Начни письмо {self.title} маркером")

stat = Stationery()
stat.draw()
pen = Pen("ErichKrause")
pen.draw()
pencil = Pencil("Конструктор")
pencil.draw()
marker = Marker("СТАММ")
marker.draw()

#Урок7
#Задание1

 class Matrix:
     def __init__(self, data):
         self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([str(itm) for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return f'Ошибка размерности матриц'

m_1 = [[3,5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [['5', '7', '27'], ['9', '23', '-54'], ['12', '3', '16']]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2

print(mtrx_1)
print('#' * 30)
print(mtrx_2)
print('#' * 30)
print(mtrx_1 + mtrx_2)
print('#' * 30)
print(new_m)
m_3 = [[3, 5, 32], [2, 4, 6], [-1,64,-8]]
m_4 = [['5', '7', '23'], ['9', '-54'],['12', '3', '16']]
print('#' * 30)
mtrx_3 = Matrix(m_3)
mtrx_4 = Matrix(m_4)
print('#' * 30)
m_3 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_4 = [['5', '7', '23'], ['12', '3', '16'], ['12', '3']]
print(mtrx_3 + mtrx_4)

#Задание2

from abc import ABC, abstractclassmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractclassmethod
    def consumption(self):
        pass
    def __abs__(self,other):
        return self.consumption + other.consumption

class Coat(Clothes):
    @property
    def consumption(self):
        print(f"Расход ткани на пошив пальто - {round(self.param / 6.5) + 0.5}")
        return round(self.param / 6.5) + 0.5

class Costume(Clothes)
    @property
    def consumption(self):
        print('Расход ткани на пошив костюма - {(2 * self.param + 0.3) / 100}')

coat = Coat(42)
costume = Costume(170)
print(coat + costume)

#Задание3
class Cell:
    def __init__(self, nums):
        self.nums = nums # 13

    def make_order(self, rows): # 5
        return '\n'.join(['*' * rows for  _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return f'Сумма ячеек: {self.nums + other.nums}'

    def __sub__(self, other):
        return  self.nums - other.nums if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше второй, вычитание невозможно!"

    def __mul__(self, other):
        return f'Множество клеток: {self.nums * other.nums}'

    def __floordiv__(self, other):
        return f'Деление клеток: {self.nums // other.nums}'

    



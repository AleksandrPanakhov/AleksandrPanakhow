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

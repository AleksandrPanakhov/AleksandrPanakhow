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



# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for number in a:
    fraction = number % 1
    if fraction != 0:
        if fraction > max:
            max = fraction
        if fraction < min:
            min = fraction
print(round(max - min, 2))
